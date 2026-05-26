# Sync Script Usage

This skill has three crawler scripts:

1. `scripts/sync_gp_wiki.py`
   Mirrors `https://developer.gp.qq.com/wikieditor`.
2. `scripts/sync_gp_api_manual.py`
   Mirrors `https://developer.gp.qq.com/api/#/`.
3. `scripts/sync_gp_docs.py`
   Wrapper that runs both of the above.

## Recommended command

Refresh everything:

```bash
python scripts/sync_gp_docs.py --force
```

## Common commands

Refresh wiki only:

```bash
python scripts/sync_gp_wiki.py
```

Refresh API manual only:

```bash
python scripts/sync_gp_api_manual.py
```

Force re-download of existing files:

```bash
python scripts/sync_gp_docs.py --force
```

Skip one source:

```bash
python scripts/sync_gp_docs.py --skip-wiki
python scripts/sync_gp_docs.py --skip-api-manual
```

Adjust API-manual concurrency:

```bash
python scripts/sync_gp_api_manual.py --workers 8
```

## Output layout

Wiki mirror:

- `references/articles/`
- `references/article-index.md`
- `references/article-index.tsv`
- `references/tree.json`

API manual mirror:

- `references/api-manual/datasets/`
- `references/api-manual/raw/`
- `references/api-manual/symbols/`
- `references/api-manual/symbol-index.md`
- `references/api-manual/symbol-index.tsv`

## Resume behavior

- `sync_gp_wiki.py` skips existing article files unless `--force` is used.
- `sync_gp_api_manual.py` skips existing symbol files unless `--force` is used.
- Both scripts prune stale generated files after rebuilding the latest index.
- If the site is unstable or the process is interrupted, rerun the same command. The scripts are designed to resume from local cache.

## Practical usage

1. Run the sync command.
2. Search the indexes with `rg`.
3. Open only the matching files.

Examples:

```bash
rg "UGCPlayerControllerSystem|APlayerController" references/api-manual/symbol-index.tsv references/api-manual/symbols
rg "航线|StartAirRoute" references/article-index.tsv references/articles
rg "观战|好友系统|聊天系统" references/article-index.tsv references/articles
```

## Notes

- The API manual is much larger than the wiki mirror. The first full sync can take several minutes.
- If the remote site returns transient SSL or timeout errors, rerun the same command. The API-manual script retries each request and supports resume behavior.
