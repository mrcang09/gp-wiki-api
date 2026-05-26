# gp-wiki-api

`gp-wiki-api` 是一个 Codex skill，用于离线查询和更新腾讯 GP / 绿洲启元 / 和平精英 UGC 相关文档镜像。

它包含两类本地资料：

- GP Wiki 文档镜像：来自 `https://developer.gp.qq.com/wikieditor`
- GP API 手册镜像：来自 `https://developer.gp.qq.com/api/#/`

适用场景包括 Lua API 查询、类 / 枚举 / 结构体符号检索、玩法系统、UI、联网、观战、社交、AI 节点、集成系统等问题。

## 目录结构

```text
gp-wiki-api/
├─ SKILL.md                         # Codex skill 入口说明
├─ agents/openai.yaml               # Codex UI 元数据
├─ scripts/
│  ├─ sync_gp_docs.py               # 同步 Wiki + API 手册
│  ├─ sync_gp_wiki.py               # 只同步 GP Wiki
│  └─ sync_gp_api_manual.py         # 只同步 GP API 手册
└─ references/
   ├─ article-index.md              # Wiki 文档目录，便于人工阅读
   ├─ article-index.tsv             # Wiki 文档目录，便于 rg 检索
   ├─ tree.json                     # Wiki 原始目录树
   ├─ sync_usage.md                 # 同步脚本说明
   ├─ articles/                     # Wiki 文档 markdown 镜像
   └─ api-manual/
      ├─ symbol-index.md            # API 符号目录，便于人工阅读
      ├─ symbol-index.tsv           # API 符号目录，便于 rg 检索
      ├─ datasets/                  # API 顶层数据集
      ├─ raw/                       # API 原始 JSON
      └─ symbols/                   # API 符号 markdown 镜像
```

## 安装到 Codex

把本仓库放到 Codex skills 目录下即可：

```powershell
git clone https://github.com/mrcang09/gp-wiki-api.git "$env:USERPROFILE\.codex\skills\gp-wiki-api"
```

如果目录已存在，先备份或删除旧目录后再 clone。

## 常用查询方式

优先从索引文件开始搜索，避免一次性加载全部资料：

```powershell
rg "APlayerController|UGCPlayerControllerSystem" references/api-manual/symbol-index.tsv references/api-manual/symbols
rg "背包系统|观战|聊天系统" references/article-index.tsv references/articles
```

找到匹配项后，再打开对应的 markdown 文件查看原文和来源链接。

## 更新本地镜像

刷新全部文档：

```powershell
python scripts/sync_gp_docs.py --force
```

只刷新 Wiki：

```powershell
python scripts/sync_gp_wiki.py
```

只刷新 API 手册：

```powershell
python scripts/sync_gp_api_manual.py
```

更多命令见 `references/sync_usage.md`。

## 使用建议

- 回答问题时优先引用本地镜像文件和原始来源 URL。
- 判断文档是否过期时，先运行同步脚本刷新索引。
- API 手册文件数量较多，搜索时优先使用 `symbol-index.tsv`。
- Wiki 文档适合查询功能说明、系统接入和编辑器流程。
- API 手册适合查询具体类、函数、枚举、结构体字段。

## 许可证

本仓库暂未声明开源许可证。仓库内容公开可见，但复用、分发和二次授权请先联系维护者确认。
