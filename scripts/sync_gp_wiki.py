#!/usr/bin/env python3
"""
Mirror the GP wiki into local markdown references for the gp-wiki-api skill.
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List
from urllib.parse import urlencode
from urllib.error import URLError
from urllib.request import Request, urlopen


BASE_URL = "https://developer.gp.qq.com/wikieditor"
LOOK_CATEGORY_URL = f"{BASE_URL}/_api/look-Category"
QUERY_ARTICLE_URL = f"{BASE_URL}/_api/query-articles"
USER_AGENT = "Codex GP Wiki Mirror/1.0"
SSL_CONTEXT = ssl.create_default_context()


def fetch_json(url: str, retries: int = 5, delay_seconds: float = 1.0) -> Dict:
    last_error = None
    for attempt in range(1, retries + 1):
        request = Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Connection": "close",
                "Cache-Control": "no-cache",
            },
        )
        try:
            with urlopen(request, timeout=60, context=SSL_CONTEXT) as response:
                return json.load(response)
        except (URLError, TimeoutError, ssl.SSLError) as exc:
            last_error = exc
            if attempt == retries:
                break
            time.sleep(delay_seconds * attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\\\|?*]+', "_", name).strip()
    name = re.sub(r"\s+", " ", name)
    return name or "untitled"


def walk_articles(nodes: Iterable[Dict], prefix: str = "") -> Iterable[Dict]:
    for node in nodes:
        label = node["label"]
        path = label if not prefix else f"{prefix} / {label}"
        if node.get("type") == 1:
            yield {"id": int(node["id"]), "title": label, "path": path}
        children = node.get("children") or []
        yield from walk_articles(children, path)


def fetch_article(article_id: int) -> Dict:
    params = urlencode({"Id": article_id})
    payload = fetch_json(f"{QUERY_ARTICLE_URL}?{params}")
    data = payload.get("data") or []
    if not data:
        raise RuntimeError(f"Article {article_id} returned no data")
    return data[0]


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def prune_stale_files(base_dir: Path, expected_files: Iterable[str]) -> int:
    expected = {(base_dir / rel_path).resolve() for rel_path in expected_files}
    removed = 0
    for path in base_dir.rglob("*.md"):
        if path.resolve() not in expected:
            path.unlink()
            removed += 1
    return removed


def build_article_markdown(article: Dict, wiki_path: str) -> str:
    title = article["Title"]
    article_id = article["Id"]
    source_url = f"{BASE_URL}/#/catalog/{article_id}"
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    lines = [
        f"# {title}",
        "",
        f"- Wiki Path: {wiki_path}",
        f"- Article ID: {article_id}",
        f"- Source URL: {source_url}",
        f"- Mirrored At (UTC): {timestamp}",
        "",
        "---",
        "",
        "## Source Content",
        "",
        article["Body"].rstrip(),
        "",
    ]
    return "\n".join(lines)


def build_index_markdown(entries: List[Dict]) -> str:
    lines = [
        "# GP Wiki Article Index",
        "",
        f"Total mirrored articles: {len(entries)}",
        "",
        "Use this file to locate the relevant article first, then open the matching file under `references/articles/`.",
        "",
    ]
    for entry in entries:
        lines.append(f"- [{entry['id']}] {entry['title']}")
        lines.append(f"  - Wiki Path: {entry['path']}")
        lines.append(f"  - URL: {entry['url']}")
        lines.append(f"  - File: {entry['file']}")
    lines.append("")
    return "\n".join(lines)


def build_index_tsv(entries: List[Dict]) -> str:
    header = "id\ttitle\twiki_path\turl\tfile"
    rows = [header]
    for entry in entries:
        rows.append(
            "\t".join(
                [
                    str(entry["id"]),
                    entry["title"].replace("\t", " "),
                    entry["path"].replace("\t", " "),
                    entry["url"],
                    entry["file"],
                ]
            )
        )
    rows.append("")
    return "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "references",
        help="Directory to write references into. Defaults to the skill references directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-fetch articles even if a local markdown file already exists.",
    )
    args = parser.parse_args()

    output_dir = args.output_dir.resolve()
    articles_dir = output_dir / "articles"
    articles_dir.mkdir(parents=True, exist_ok=True)

    category_payload = fetch_json(LOOK_CATEGORY_URL)
    category_data = category_payload.get("data") or []
    if not category_data:
        raise RuntimeError("Category tree returned no data")

    tree_body = category_data[0]["Body"]
    tree = json.loads(tree_body)
    article_nodes = sorted(walk_articles(tree), key=lambda item: item["id"])

    index_entries: List[Dict] = []
    for idx, node in enumerate(article_nodes, start=1):
        filename = f"{node['id']}-{sanitize_filename(node['title'])}.md"
        file_path = articles_dir / filename

        if args.force or not file_path.exists():
            article = fetch_article(node["id"])
            filename = f"{article['Id']}-{sanitize_filename(article['Title'])}.md"
            file_path = articles_dir / filename
            markdown = build_article_markdown(article, node["path"])
            write_text(file_path, markdown)
            time.sleep(0.1)

        index_entries.append(
            {
                "id": int(node["id"]),
                "title": node["title"],
                "path": node["path"],
                "url": f"{BASE_URL}/#/catalog/{node['id']}",
                "file": f"articles/{filename}",
            }
        )
        if idx % 25 == 0:
            print(f"Indexed {idx}/{len(article_nodes)} articles...")

    write_text(output_dir / "tree.json", json.dumps(tree, ensure_ascii=False, indent=2))
    write_text(output_dir / "article-index.md", build_index_markdown(index_entries))
    write_text(output_dir / "article-index.tsv", build_index_tsv(index_entries))

    removed = prune_stale_files(articles_dir, [entry["file"].replace("articles/", "", 1) for entry in index_entries])
    if removed:
        print(f"Removed {removed} stale article files.")

    print(f"Mirrored {len(index_entries)} articles into {output_dir}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(f"[ERROR] {exc}", file=sys.stderr)
        raise
