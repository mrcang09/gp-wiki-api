#!/usr/bin/env python3
"""
Mirror the GP API manual into local references for the gp-wiki-api skill.
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Tuple
from urllib.error import URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


BASE_URL = "https://developer.gp.qq.com/api/"
USER_AGENT = "Codex GP API Mirror/1.0"
SSL_CONTEXT = ssl.create_default_context()
DATASET_PATHS = {
    "class_list": "class/list/list.json",
    "class_tree": "class/list/tree.json",
    "class_sorted": "class/list/sorted_list.json",
    "enum_sorted": "cppenum/list/sorted_list.json",
    "struct_sorted": "cppstruct/list/sorted_list.json",
    "globalfunc_sorted": "globalfunc/list/sorted_list.json",
}


def fetch_text(url: str, retries: int = 5, delay_seconds: float = 1.0) -> str:
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
                return response.read().decode("utf-8", errors="replace")
        except (URLError, TimeoutError, ssl.SSLError) as exc:
            last_error = exc
            if attempt == retries:
                break
            time.sleep(delay_seconds * attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def fetch_json(url: str) -> Dict:
    return json.loads(fetch_text(url))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, payload: Dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def prune_stale_files(search_dir: Path, expected_files: Iterable[Path], suffix: str) -> int:
    expected = {path.resolve() for path in expected_files}
    removed = 0
    for path in search_dir.rglob(f"*{suffix}"):
        if path.resolve() not in expected:
            path.unlink()
            removed += 1
    return removed


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]+', "_", name).strip()
    name = re.sub(r"\s+", " ", name)
    return name or "untitled"


def normalize_api_path(rel_path: str) -> str:
    if rel_path.startswith("detail/class/"):
        return "class/detail/" + rel_path[len("detail/class/") :]
    if rel_path.startswith("detail/cppenum/"):
        return "cppenum/detail/" + rel_path[len("detail/cppenum/") :]
    if rel_path.startswith("detail/cppstruct/"):
        return "cppstruct/detail/" + rel_path[len("detail/cppstruct/") :]
    if rel_path.startswith("detail/globalfunc/"):
        return "globalfunc/detail/" + rel_path[len("detail/globalfunc/") :]
    return rel_path


def flatten_class_category_list(nodes: Iterable[Dict], prefix: str = "") -> Dict[str, str]:
    mapping: Dict[str, str] = {}
    for node in nodes:
        label = node["Label"]
        node_type = node["Type"]
        current = label if not prefix else f"{prefix} / {label}"
        if node_type == "directory":
            children = node.get("Children") or []
            mapping.update(flatten_class_category_list(children, current))
        else:
            mapping[node["Name"]] = current
    return mapping


def flatten_sorted_map(kind: str, payload: Dict) -> List[Dict]:
    entries: List[Dict] = []

    def walk(obj: Dict) -> None:
        for key, value in obj.items():
            if isinstance(value, str) and value.endswith(".json"):
                entries.append(
                    {
                        "kind": kind,
                        "name": key,
                        "rel_path": normalize_api_path(value),
                    }
                )
            elif isinstance(value, dict):
                walk(value)

    walk(payload)
    entries.sort(key=lambda item: (item["kind"], item["name"]))
    return entries


def build_table(headers: List[str], rows: List[List[str]]) -> List[str]:
    if not rows:
        return []
    output = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        clean = [cell.replace("\n", "<br>") if cell else "" for cell in row]
        output.append("| " + " | ".join(clean) + " |")
    output.append("")
    return output


def render_variable_rows(items: List[Dict], enum_mode: bool = False) -> List[List[str]]:
    rows: List[List[str]] = []
    for item in items or []:
        if enum_mode:
            rows.append(
                [
                    str(item.get("Name", "")),
                    str(item.get("Value", "")),
                    str(item.get("Description", "")),
                ]
            )
        else:
            rows.append(
                [
                    str(item.get("Name", "")),
                    str(item.get("Type", "")),
                    str(item.get("Description", "")),
                    str(item.get("Redirect", "")),
                ]
            )
    return rows


def render_param_rows(items: List[Dict]) -> List[List[str]]:
    rows: List[List[str]] = []
    for item in items or []:
        rows.append(
            [
                str(item.get("Name", "")),
                str(item.get("Type", "")),
                str(item.get("Description", "")),
                str(item.get("Redirect", "")),
            ]
        )
    return rows


def build_symbol_markdown(entry: Dict, detail: Dict) -> str:
    source_url = BASE_URL + quote(entry["rel_path"], safe="/")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    lines = [
        f"# {detail.get('Name') or entry['name']}",
        "",
        f"- Symbol Type: {entry['kind']}",
        f"- Symbol Path: {entry.get('display_path', '') or entry['name']}",
        f"- Source JSON Path: {entry['rel_path']}",
        f"- Source JSON URL: {source_url}",
        f"- Mirrored At (UTC): {timestamp}",
        "",
        "---",
        "",
    ]

    description = str(detail.get("Description") or "").strip()
    if description:
        lines.extend(["## Description", "", description, ""])

    variables = detail.get("Variables") or []
    if variables:
        lines.extend(["## Variables", ""])
        if entry["kind"] == "enum":
            lines.extend(build_table(["Name", "Value", "Description"], render_variable_rows(variables, enum_mode=True)))
        else:
            lines.extend(
                build_table(
                    ["Name", "Type", "Description", "Redirect"],
                    render_variable_rows(variables),
                )
            )

    functions = detail.get("Functions") or []
    if functions:
        lines.extend(["## Functions", ""])
        for function in functions:
            lines.append(f"### {function.get('Name', '')}")
            lines.append("")
            func_desc = str(function.get("Description") or "").strip()
            if func_desc:
                lines.append(func_desc)
                lines.append("")

            params = function.get("Params") or []
            if params:
                lines.append("Parameters:")
                lines.append("")
                lines.extend(
                    build_table(
                        ["Name", "Type", "Description", "Redirect"],
                        render_param_rows(params),
                    )
                )

            returns = function.get("Return") or []
            if returns:
                lines.append("Returns:")
                lines.append("")
                lines.extend(
                    build_table(
                        ["Name", "Type", "Description", "Redirect"],
                        render_param_rows(returns),
                    )
                )

    params = detail.get("Params") or []
    if params and entry["kind"] == "globalfunc":
        lines.extend(["## Parameters", ""])
        lines.extend(
            build_table(
                ["Name", "Type", "Description", "Redirect"],
                render_param_rows(params),
            )
        )

    returns = detail.get("Return") or []
    if returns and entry["kind"] == "globalfunc":
        lines.extend(["## Returns", ""])
        lines.extend(
            build_table(
                ["Name", "Type", "Description", "Redirect"],
                render_param_rows(returns),
            )
        )

    return "\n".join(lines).rstrip() + "\n"


def build_symbol_index_markdown(entries: List[Dict]) -> str:
    counts: Dict[str, int] = {}
    for entry in entries:
        counts[entry["kind"]] = counts.get(entry["kind"], 0) + 1

    lines = [
        "# GP API Manual Index",
        "",
        f"Total mirrored symbols: {len(entries)}",
        "",
        "Counts by type:",
        "",
    ]
    for kind in sorted(counts):
        lines.append(f"- {kind}: {counts[kind]}")
    lines.extend(
        [
            "",
            "Use `symbol-index.tsv` for grep-friendly lookup.",
            "",
        ]
    )

    for entry in entries:
        lines.append(f"- [{entry['kind']}] {entry['name']}")
        lines.append(f"  - Symbol Path: {entry.get('display_path', '') or entry['name']}")
        lines.append(f"  - Source JSON Path: {entry['rel_path']}")
        lines.append(f"  - Source JSON URL: {entry['source_url']}")
        lines.append(f"  - Markdown File: {entry['markdown_file']}")
        lines.append(f"  - Raw File: {entry['raw_file']}")
    lines.append("")
    return "\n".join(lines)


def build_symbol_index_tsv(entries: List[Dict]) -> str:
    header = "kind\tname\tsymbol_path\tsource_json_path\tsource_json_url\tmarkdown_file\traw_file\tdescription"
    rows = [header]
    for entry in entries:
        rows.append(
            "\t".join(
                [
                    entry["kind"],
                    entry["name"].replace("\t", " "),
                    (entry.get("display_path", "") or entry["name"]).replace("\t", " "),
                    entry["rel_path"],
                    entry["source_url"],
                    entry["markdown_file"],
                    entry["raw_file"],
                    entry.get("description", "").replace("\t", " ").replace("\n", " "),
                ]
            )
        )
    rows.append("")
    return "\n".join(rows)


def sync_one(entry: Dict, output_dir: Path, force: bool) -> Dict:
    file_name = sanitize_filename(entry["name"])
    markdown_rel = Path("symbols") / entry["kind"] / f"{file_name}.md"
    raw_rel = Path("raw") / entry["kind"] / f"{file_name}.json"
    markdown_path = output_dir / markdown_rel
    raw_path = output_dir / raw_rel

    if not force and markdown_path.exists() and raw_path.exists():
        entry["markdown_file"] = markdown_rel.as_posix()
        entry["raw_file"] = raw_rel.as_posix()
        return entry

    source_url = BASE_URL + quote(entry["rel_path"], safe="/")
    detail = fetch_json(source_url)
    entry["source_url"] = source_url
    entry["description"] = str(detail.get("Description") or "").strip()
    entry["markdown_file"] = markdown_rel.as_posix()
    entry["raw_file"] = raw_rel.as_posix()

    write_json(raw_path, detail)
    write_text(markdown_path, build_symbol_markdown(entry, detail))
    return entry


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "references" / "api-manual",
        help="Directory to write the mirrored API manual into.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Number of concurrent fetch workers.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-fetch symbols even if local files already exist.",
    )
    args = parser.parse_args()

    output_dir = args.output_dir.resolve()
    datasets_dir = output_dir / "datasets"
    datasets_dir.mkdir(parents=True, exist_ok=True)

    datasets = {}
    for key, rel_path in DATASET_PATHS.items():
        payload = fetch_json(BASE_URL + rel_path)
        datasets[key] = payload
        write_json(datasets_dir / f"{key}.json", payload)

    class_display_paths = flatten_class_category_list(datasets["class_list"])
    entries: List[Dict] = []
    entries.extend(flatten_sorted_map("class", datasets["class_sorted"]))
    entries.extend(flatten_sorted_map("enum", datasets["enum_sorted"]))
    entries.extend(flatten_sorted_map("struct", datasets["struct_sorted"]))
    entries.extend(flatten_sorted_map("globalfunc", datasets["globalfunc_sorted"]))

    for entry in entries:
        entry["display_path"] = class_display_paths.get(entry["name"], entry["name"]) if entry["kind"] == "class" else entry["name"]
        entry["source_url"] = BASE_URL + quote(entry["rel_path"], safe="/")
        entry["description"] = ""

    mirrored: List[Dict] = []
    failures: List[Tuple[str, str]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        future_map = {executor.submit(sync_one, entry, output_dir, args.force): entry for entry in entries}
        for index, future in enumerate(as_completed(future_map), start=1):
            entry = future_map[future]
            try:
                mirrored.append(future.result())
            except Exception as exc:
                failures.append((entry["name"], str(exc)))
            if index % 100 == 0:
                print(f"Processed {index}/{len(entries)} symbols...")

    mirrored.sort(key=lambda item: (item["kind"], item["name"]))
    removed_markdown = prune_stale_files(
        output_dir / "symbols",
        [output_dir / entry["markdown_file"] for entry in mirrored],
        ".md",
    )
    removed_raw = prune_stale_files(
        output_dir / "raw",
        [output_dir / entry["raw_file"] for entry in mirrored],
        ".json",
    )
    write_text(output_dir / "symbol-index.md", build_symbol_index_markdown(mirrored))
    write_text(output_dir / "symbol-index.tsv", build_symbol_index_tsv(mirrored))

    if removed_markdown or removed_raw:
        print(f"Removed {removed_markdown} stale symbol markdown files and {removed_raw} stale raw files.")

    print(f"Mirrored {len(mirrored)} symbols into {output_dir}")
    if failures:
        print(f"[ERROR] {len(failures)} symbols failed", file=sys.stderr)
        for name, error in failures[:20]:
            print(f"- {name}: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
