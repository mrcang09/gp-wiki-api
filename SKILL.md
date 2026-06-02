---
name: gp-wiki-api
description: Use when the task involves Tencent GP / Oasis Era documentation from developer.gp.qq.com/wikieditor or developer.gp.qq.com/api, especially Lua APIs, API-manual symbol lookup, Peace Elite integrated systems, gameplay systems, UI integration, networking, spectate or social features, AI nodes, or when you need to find the original local mirror and cite it.
---

# GP Wiki API

## When to use
- Answer questions about the GP wiki at `developer.gp.qq.com/wikieditor`.
- Answer questions about the GP API manual at `developer.gp.qq.com/api/#/`.
- Look up Oasis Era / Peace Elite UGC Lua APIs, class APIs, enum values, struct fields, global functions, gameplay systems, networking rules, UI integration, AI nodes, or platform-integrated features.
- Map a user problem to the original mirrored article or API symbol and quote or summarize the exact local document.
- Answer Oasis Era upload, test upload vs publish upload, project binding, review submission, grey release, signing, revenue, planning-doc, and compliance questions using the submission-flow notes.
- Refresh the local mirrors when the user asks for the latest docs or when the cached copy looks stale.

## Workflow
1. Decide whether the question belongs to the wiki mirror or the API-manual mirror.
2. Start with the index files:
   - Wiki: `references/article-index.md` or `references/article-index.tsv`
   - API manual: `references/api-manual/symbol-index.md` or `references/api-manual/symbol-index.tsv`
   - Search by keyword first.
   - Do not load the whole corpus into context.
3. Open only the matching files:
   - Wiki: `references/articles/`
   - API manual: `references/api-manual/symbols/`
4. If the docs might be outdated, run:
   - `python scripts/sync_gp_docs.py --force`
5. In the answer:
   - cite the local file and the original source URL
   - distinguish documented facts from your inference
   - if multiple sources overlap, explain which source covers what

## Reference Map
- `docs/绿洲提审流程速查.md`
  Curated notes for Oasis Era upload, test upload vs publish upload, project binding, first submission, update submission, grey release, signing, copyright/compliance, and revenue questions.
- `docs/中文说明.md`
  Chinese overview of this skill, common lookup commands, and local maintenance notes.
- `references/article-index.md`
  Human-readable catalog of all mirrored articles with wiki paths and local filenames.
- `references/article-index.tsv`
  Grep-friendly index: `id`, `title`, `wiki_path`, `url`, `file`.
- `references/tree.json`
  Raw category tree from the wiki.
- `references/articles/`
  One markdown file per mirrored article.
- `references/api-manual/symbol-index.md`
  Human-readable catalog of mirrored API-manual symbols.
- `references/api-manual/symbol-index.tsv`
  Grep-friendly index for classes, enums, structs, and global functions.
- `references/api-manual/datasets/`
  Top-level API-manual dataset JSON files.
- `references/api-manual/raw/`
  Raw mirrored detail JSON files.
- `references/api-manual/symbols/`
  Rendered markdown files for API-manual symbols.
- `references/sync_usage.md`
  How to run the crawler scripts and what they generate.

## Search Patterns
Use `rg` first, then open only the relevant article files.

Examples:
```bash
rg "UGCPlayerControllerSystem|APlayerController|TagLogFormatPrint" references/api-manual/symbol-index.tsv references/api-manual/symbols
rg "enum|struct|globalfunc" references/api-manual/symbol-index.tsv
rg "AirRoute|StartAirRoute|route" references/article-index.tsv references/articles
rg "spectate|friend|chat" references/article-index.tsv references/articles
rg "network|EventSystem|RPC" references/article-index.tsv references/articles
rg "custom panel|AddChildToTochButton|notch" references/article-index.tsv references/articles
rg "AI|behavior tree|custom node|interface" references/article-index.tsv references/articles
rg "测试上传|发布上传|提审|签约|灰度|策划案|jobid" docs references/article-index.tsv references/articles
```

## Practical Reading Order
For broad questions, narrow scope in this order:

1. Framework and lifecycle:
   - `346` Lua guide
   - `352` gameplay framework
   - `203` networking
2. UI and integrated systems:
   - `204` custom panel
   - `347` UI quick start
   - `357` notch screen adaptation
3. Social and spectate:
   - `208`, `209`, `210`, `213`, `216`
4. Gameplay and AI:
   - `206`, `173`, `358`
5. Upload, submission, teams, and release:
   - `docs/绿洲提审流程速查.md`
   - `372` upload project and real-device testing
   - `378` gameplay submission and version update
   - `380` team-account workflow
   - `20314` upload and debugging

## Oasis Submission, Upload, and Signing Flow

Primary local reference:
- `docs/绿洲提审流程速查.md`

Use this section for questions about:
- test upload vs publish upload
- why an uploaded version is not visible in the management backend
- UID whitelist testing
- project binding and `jobid`
- first review submission
- version update submission
- grey release / "抢先体验专区"
- personal or team signing
- planning-doc, copyright, AI-content, random-play, and commercial-compliance materials

Must-remember facts:
- Test upload is for internal real-device testing and whitelist verification. It cannot be bound to a management-platform project and cannot be selected for review submission.
- Publish upload is the path for formal environment deployment, project binding, version creation, review submission, grey release, and later update submissions.
- If the backend cannot see an uploaded version, first check whether the user used publish upload, whether the uploader belongs to the same team as the project, whether the version was already bound, whether it is still among the latest 3 unbound versions, and whether the upload has had enough time to finish server push.
- Upload completion can mean the bake finished; backend or client visibility may still be delayed, commonly within 10 minutes.
- Submission requires the account to belong to a team. Personal developers can create a team and submit through that team.
- First submission generally follows: onboarding and qualification, planning-doc review, development, test upload and UID whitelist testing, publish upload and record `jobid`, create/bind project in the management platform, add version, fill assets/materials/compliance self-checks, submit review.
- Review covers content compliance, legal/copyright risk, unfair-competition risk, gameplay bugs, and extra commercial-play testing when monetization is involved.
- Grey release happens after review and testing pass. It usually goes through "抢先体验专区", can repeat several rounds, and each round commonly takes 1-3 days.
- Signing can run in parallel with grey testing after review passes. Personal and team signing both start from the management-platform signing entrance opened by officials.
- Version updates do not usually require a new project or new signing. Publish upload a new version, record `jobid`, submit update review from the existing project, and fill player-facing update notes plus content-change explanations.

## Oasis DS EmmyLua Debugging Pitfall
Use this checklist when troubleshooting Oasis Era / GP PIE DS Lua debugging, especially when breakpoints do not bind or VSCode shows `Connected.` and then immediately disconnects.

Primary local reference:
- Wiki article `references/articles/20272-EmmyLua调试工具.md`, source `https://developer.gp.qq.com/wikieditor/#/catalog/20272`.

Documented facts from the article:
- EmmyLua supports remote DS debugging.
- `Debug Mode` should be `EMMY LUA`.
- `Wait IDE` is recommended so DS waits for VSCode during startup.
- `Auto Generate VSCode Config` is required for remote DS Lua script debugging.
- The debug target list uses `PIE0` for local client, `DS` for remote server, and `PIE/DS` when both sides are debuggable.

Observed boundary case:
- DS Lua runs in the remote/container DS environment, not in a local Windows DS process. Do not look for a local DS process to attach to.
- The local scripts are uploaded into a DS-side path such as `UGCProjects/_<debug-id>/<project>/`.
- VSCode connects to the DS Lua VM through the EmmyLua TCP bridge, commonly on a `198.18.0.x:<port>` address. This is remote debugging, not local process attach.
- A successful TCP test only proves the bridge port is reachable. It does not prove EmmyLua protocol handshaking succeeded.
- `Connected.` in the VSCode Debug Console can be printed by the EmmyLua debug adapter immediately after TCP connect. It can still disconnect right after that while sending `InitReq`, breakpoints, or `ReadyReq`.
- If the debug adapter reports `ECONNABORTED` or the socket disappears after `Connected.`, treat it as a DS EmmyLua bridge/protocol failure or plugin-version mismatch, not as a breakpoint-location problem.

Recommended diagnosis flow:
1. Find the current DS debug port from the newest DS realtime log under `Saved/Logs/<project>/DSlog/FullLog/`.
   - Search for `OverrideVsCodePort=`, `VsCodePort=`, or `IsServer EmmyDebug Beging tcpListen`.
   - Do not reuse an older PIE run's port; it can change between PIE launches.
2. Confirm TCP reachability:
   - PowerShell: `Test-NetConnection -ComputerName 198.18.0.2 -Port <port>`
3. Confirm VSCode launch config points to the same DS port:
   - `.vscode/launch.json`
   - workspace-level `workspace.code-workspace` `launch.configurations`, if present.
   - Watch for Oasis auto-generating `.vscode/launch.json` back to `PIE0` / `9966`.
4. Confirm the selected debug config is `DS` / `DS Local (server)`, not `PIE0`.
5. Confirm the target breakpoint is in server-side Lua code and is enabled.
6. If VSCode prints `Connected.` but no persistent connection remains and the adapter errors with `ECONNABORTED`, the local port/config/breakpoint checks have passed. Next likely causes are:
   - EmmyLua VSCode plugin version incompatible with the DS-side bridge.
   - DS-side EmmyLua bridge bug or stale DS session.
   - Editor-generated launch config missing a hidden required field.

Practical next actions for this failure mode:
- Restart PIE/DS and re-read the new `OverrideVsCodePort`.
- Let Oasis auto-generate the official launch config and compare it before hand-editing.
- Try a different EmmyLua plugin version if the platform team recommends one.
- If the same `Connected.` then `ECONNABORTED` result persists with the official generated config and current port, escalate as a platform/DS debug bridge issue rather than continuing to move Lua breakpoints.

## Refreshing the Mirrors
Run this when the user explicitly asks for the latest docs or when the local mirror is missing content:

```bash
python scripts/sync_gp_docs.py --force
```

Optional output path:

```bash
python scripts/sync_gp_wiki.py --output-dir references
python scripts/sync_gp_api_manual.py --output-dir references/api-manual
```

See `references/sync_usage.md` for script-specific commands and outputs.

The sync scripts rebuild the indexes and prune stale generated article/symbol files so local search does not return documents that have been removed or renamed upstream.

## Expectations
- Prefer the local mirrors over ad hoc browsing when answering GP documentation questions.
- Keep answers grounded in the mirrored docs.
- If the user asks for a new summary or a derived handbook, generate it from the local references instead of re-scraping everything.
