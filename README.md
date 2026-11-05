# TxtPush —— 通用小说知识库 + 自动化创作流水线

面向**各类题材**（现实、言情、悬疑、玄幻、历史、武侠、科幻……）的小说创作系统：
**33 篇方法论知识库** 动态注入 **9 阶段智能创作流水线**，从一句题材关键词一路产出
「概念 → 世界设定 → 角色 → 大纲 → 逐章正文 → 逐章审校 → 修订 → 全书连续性审校 → 汇编成书 → 出版级导出（EPUB / HTML / TXT）」。

**纯 Python 标准库实现（Python 3.8+），零第三方依赖，跨平台（Windows / macOS / Linux）通用。**

> 与同门项目 `FutureTxt`（科幻专用）的关系：架构同源，知识库与提示词全面通用化；
> 科幻只是本流水线支持的一种题材（`--genre 科幻`），不再是唯一。

---

## 核心亮点与系统能力

- 🧠 **33 篇通用小说方法论知识库**：概论与类型定位、世界设定（现实/架空通用）、角色与对手、情节结构（三幕/起承转合/单元剧）、文风叙事、素材创意、72 条审稿自查清单、**质量红线**、**短篇工艺**，外加 **7 个题材模块**（言情 / 悬疑推理 / 玄幻奇幻 / 都市现实 / 历史 / 武侠仙侠 / 科幻）。
- 🎯 **题材感知（`--genre`）**：选定题材后自动挂载对应写作要点模块；题材只影响注入知识，不锁死任何能力——不选（默认「通用」）即全题材通吃。
- 📐 **两种作品形态（`--form`）**：`novel` 长篇多章（默认，章数可固定或由情节自定）/ `short` **短篇单篇**——单篇结构方案（单一效果·一个转折·结尾不解释）、单章流水线与专属红线，全篇字数由 `--words` 指定（默认 6000）。
- 🚦 **文稿质量红线（`08-质量规则`）**：跨章唯一、数字自洽、字数闸门、文本卫生、视角纪律、**镜面原则（映射当下）**——自动注入写作/审校/修订/连续性四个阶段，并由机器检查强制兜底。
- 🪞 **镜面原则·映射当下**：题材可以架空，人心必须真实——每项核心设定或矛盾都要照见一种可辨认的现实结构（生存/金钱/权力/关系/身份/职业），并以**人物付出的具体代价**显形；概念与设定阶段强制产出「现实映射表」。
- 🧪 **确定性文风体检（`lint`）**：零 API 成本检测陈词滥调、AI 腔句式、超长句、重复整句/段首、虚词密度与高频四字串，给出 0–100 体检分；摘要自动注入审校/修订提示词。
- 🔍 **轻量动态 RAG 与相关度重排**：正文起草时根据每章剧情大纲，自动动态检索匹配的方法论/题材小节并定向注入；知识库全文检索支持相关度打分排序。
- 📊 **小说数据全景与文学工艺指标（`stats`）**：全书规模统计、默读与演播时长换算、字数波动分析、章节篇幅柱状图、对白占比（警惕说明文过载）与核心角色聚光灯。
- 🛡️ **设定与伏笔闭环审计引擎（`audit`）**：自动索引硬性设定（W1..Wn）与角色一致性规则（C1..Cn），扫描大纲未兑现伏笔、幽灵回收以及正文超长单段说明文（Infodump）。
- 📚 **出版级多格式导出（`export`）**：
  - **EPUB 3.0**：符合 IDPF 标准（未压缩 mimetype、NCX/Nav 目录、扉页与中文排版 CSS，可直推 Apple Books、微信读书、Kindle 等）；
  - **HTML 沉浸式离线阅读器**：单文件离线网页，亮暗主题切换、字号缩放、侧栏目录与阅读进度；
  - **规范排版 TXT**：全角段首缩进与标准分隔。
  - 导出自动剥离审校锚点（W/C 编号、日常细节清单、条目标题标签）产出**出版净稿**，章节与成书保留标记供审校与 `audit` 溯源。
- 🌏 **双语发行（`translate`）**：先生成中英术语表（人名/地名/机构/称谓统一），再逐章译为出版级英文；`export --lang en` 输出英文版三格式。
- 🚀 **一键发行（`release`）**：打包 ASCII 附件（GitHub 资产名不支持中文）、自动生成双语发行说明、创建/更新 GitHub Release，版本号自动递增。
- 🌐 **随身 Web 端（`web/`）**：免服务器的 PWA 创作工作台（知识库检索、流式生成、浏览器端打包 EPUB/HTML/TXT），可部署到 GitHub Pages。
- 🩺 **系统自检（`doctor`）**：环境体检、知识库完整性校验、API 连通性与网络延迟。
- 🛡️ **生产级 LLM 通信守护**：SSE 流式保活（抗网络掐断）、指数退避重试、思考模型 token 耗尽自动加倍、Token 用量与成本分阶段统计。

---

## 目录结构

```
TXTPush/
├── knowledge/                 # 通用小说写作知识库（33 篇）
│   ├── 01-概论/               # 讲故事的本质、类型全景与定位、主题与立意
│   ├── 02-世界设定/           # 设定方法论、规则体系与代价、社会质感、时代与日常细节
│   ├── 03-角色/               # 角色构建、关系与对手、对话与语言指纹
│   ├── 04-情节结构/           # 整体结构节奏、章节与钩子、冲突与悬念、高潮与结局
│   ├── 05-文风与叙事/         # 叙述视角、描写与沉浸感、语言节奏与风格
│   ├── 06-素材与创意/         # 灵感方法、套路清单、反套路与创新
│   ├── 07-参考/               # 审稿自查清单（72 条）、类型速查、修改示例与病句诊所
│   ├── 08-质量规则/           # 文稿质量红线、镜面原则
│   ├── 09-短篇写作/           # 短篇形态专属（--form short 自动注入）
│   └── 10-题材模块/           # 言情/悬疑推理/玄幻奇幻/都市现实/历史/武侠仙侠/科幻（--genre 自动注入）
├── pipeline/                  # 自动化流水线
│   ├── run.py                 # 统一命令行入口（多子命令 + 彩色终端）
│   ├── stages.py              # 9 阶段提示词工程、状态记忆池、质量红线/字数闸门/完结保护/机器预检
│   ├── style.py               # 确定性文风体检：套话/AI 腔/长句/重复/相似章/虚词密度
│   ├── llm.py                 # 生产级 OpenAI 兼容客户端（流式保活、用量追踪、截断扩充）
│   ├── kb.py                  # 知识库均衡预算加载、形态与题材模块挂载、检索与局部动态 RAG
│   ├── export.py              # 纯标准库 EPUB 3.0 / 单文件 HTML 阅读器 / 规范 TXT 导出
│   ├── analytics.py           # 小说全景统计、对白占比、篇幅分布、角色聚光灯
│   ├── audit.py               # 设定 W/C 规则与大纲伏笔闭环审计
│   ├── translate.py           # 中文 → 英文双语支线（术语表 + 逐章翻译）
│   ├── release.py             # 一键发行：ASCII 附件打包 + 双语说明 + GitHub Release
│   ├── doctor.py              # 环境、知识库与端点连通性自检
│   └── bundle_kb.py           # 知识库打包（Web 端离线知识包）
├── tests/                     # 自动化单元测试套件（零外部依赖，一键运行）
├── web/                       # 免服务器 PWA 创作端（离线缓存、浏览器端 EPUB 打包）
├── benchmark_models.py        # 候选模型横测工具（延迟 + 中文创作质量）
├── projects/<项目名>/         # 每本小说一个独立工作区
│   ├── project.json           # 书名、题材（genre）、关键词、章数、字数、视角等配置
│   ├── state.json             # 阶段状态、逐章摘要与 Token 用量（断点续跑）
│   ├── 00-创作概念.md
│   ├── 01-世界设定.md
│   ├── 02-角色.md
│   ├── 03-大纲.md
│   ├── chapters/chapter_*.md  # 逐章正文（修订自动 .bak 备份）
│   ├── reviews/chapter_*_审校.md  # 逐章审校报告
│   ├── reviews/全书连续性报告.md   # 跨章重复/矛盾机器预检 + LLM 复核
│   ├── manuscript/《书名》·初稿.md
│   ├── dist/                  # 中文出版交付物（.epub / .html / .txt）
│   ├── chapters_en/  glossary_en.md  blurb_en.md  dist_en/   # 英文版链路
├── config.json                # LLM API 配置（不入库密钥，见下）
└── README.md
```

---

## 快速开始

### 1. 系统自检

```
python pipeline/run.py doctor
```

### 2. 配置 API 端点

支持任何 OpenAI 兼容接口（DeepSeek、月之暗面、通义千问、OpenAI、NVIDIA NIM、vLLM、Ollama 等）：

```
python pipeline/run.py config --api-key sk-xxx \
    --base-url https://api.deepseek.com/v1 --model deepseek-chat
```

或设置环境变量：`TXTPUSH_API_KEY`、`TXTPUSH_BASE_URL`、`TXTPUSH_MODEL`。

### 3. 创建小说项目

```
python pipeline/run.py init 长夜将尽 \
    --genre 悬疑推理 \
    --keywords "小镇,旧案,返乡,救赎" \
    --premise "一位返乡青年在父亲遗物中发现旧账本，牵出小镇二十年前的旧案" \
    --chapters 12 --words 3000 --pov "第三人称有限" --tone "克制、凝练、有画面感"
```

**题材（`--genre`）**：`通用`（默认）/ `言情` / `悬疑推理` / `玄幻奇幻` / `都市现实` / `历史` / `武侠仙侠` / `科幻`——
选定后自动注入 `knowledge/10-题材模块/` 对应要点；不选即不挂载题材模块，全凭通用知识库写作。

**章数模式（`--chapters-mode`）**：`fixed`（默认）严格写死章数；`auto` **章数由情节决定**（大纲成为章数的唯一权威，建议 `--min-chapters`~`--max-chapters`）。

**作品形态（`--form`）**：`novel` 长篇多章（默认）/ `short` 短篇单篇。

```
python pipeline/run.py init 末班车 --form short --words 6000 --genre 都市现实 \
    --premise "末班公交上，售票员认出一个每天坐同一班车的乘客，其实早已搬离这座城市三年"
```

**项目级知识模块（`--kb-modules`）**：把自定义/题材专用模块挂到单个项目，逗号分隔，例如 `--kb-modules 10-题材模块/悬疑推理`。

### 4. 一键跑通全流程

```
python pipeline/run.py run 长夜将尽
```

### 5. 查看进度与 Token 消耗

```
python pipeline/run.py status 长夜将尽
```

---

## 流水线 9 阶段

| 阶段 | 产物 | 知识库注入重点 | 说明 |
|---|---|---|---|
| `concept` | 00-创作概念.md | 概论、素材与创意、质量规则 | Logline、三层冲突、主题、**现实映射表**、结局与创新点 |
| `world` | 01-世界设定.md | 设定方法论、规范与代价、日常细节、质量规则 | 舞台/规则体系/编年史/社会与日常 + **硬性设定 W1…Wn** 铁律清单 |
| `characters` | 02-角色.md | 角色构建、关系与对手、文化日常 | 欲望/需求/缺陷/秘密/弧光/语言指纹 + **一致性要点 C1…Cn** |
| `outline` | 03-大纲.md | 情节结构、素材与创意、主题 | 精确 N 章三幕式展开：目标/冲突/转折/揭示/伏笔/钩子 |
| `draft` | chapters/\*.md | **质量规则**、文风叙事、情节结构、动态题材片段 | 逐章创作：前情摘要 + 邻章大纲 + 上章结尾衔接 + 局部 RAG + **质量红线**；**字数闸门**（<85% 自动扩写/续写） |
| `review` | reviews/\*_审校.md | **质量规则**、72 条审稿清单、类型速查 | 对照硬规则打分（1-10）；注入相邻章摘要，**必查跨章重复/数值矛盾/钩子雷同** |
| `revise` | 覆盖正文（.bak 备份） | **质量规则**、文风叙事、情节结构 | 注入大纲+前情+下一章摘要+连续性报告，**禁止引入他章已有场景**；结论「可直接通过」智能跳过 |
| `continuity` | reviews/全书连续性报告.md | **质量规则**、审稿清单 | **机器预检**（跨章重复整句/雷同结尾/相似章/收尾异常/字数/卫生）+ LLM 跨章复核 |
| `assemble` | manuscript/初稿.md + dist/\* | 全书合并 | `clean()` 清洗 + 全书字数闸门告警，自动生成 EPUB、HTML、TXT |

### 质量红线（写进提示词 + 机器兜底）

1. **跨章唯一**：场景桥段/结尾句/名句全书只出现一次；由「前情摘要 + 连续性审校 + 机器重复句预检」三层拦截；
2. **字数只认脚本统计**：模型自报字数虚报可达 28%，一律以 `word_count()` 为准；不足 85% 触发两段式闸门（整体扩写 → 沿章尾续写，附复述/重启拦截护栏与完结保护）；
3. **任何项目不得跳过审校链**：`review → revise → continuity` 缺一不可；
4. **镜面原则·映射当下**：设定照见现实，代价必须显形（概念/设定阶段强制产出映射表，审校逐条核对）。

---

## 常用进阶命令

### 文学工艺指标（`stats`）

```
python pipeline/run.py stats 长夜将尽
```

输出：全书字数、段落数、默读/演播时长、章节篇幅极差与标准差、终端柱状图、对白占比、角色出场频次聚光灯。

### 设定与伏笔审计（`audit`）

```
python pipeline/run.py audit 长夜将尽
```

校验 W/C 规则覆盖度、伏笔与回收链路，标记正文单段超标（Infodump 风险）。

### 文风体检（`lint`，零 API 成本）

```
python pipeline/run.py lint 长夜将尽            # 全书体检
python pipeline/run.py lint 长夜将尽 --chapter 3
python pipeline/run.py lint 长夜将尽 --write    # 报告写入 reviews/文风体检.md
python pipeline/run.py lint --all --write       # 全库总览
```

检测陈词滥调、AI 腔句式、超长句、重复整句/段首、跨章高度相似（复制章）、多重收尾、虚词口头禅密度、高频四字串，给出 0–100 分；摘要自动注入审校与修订提示词。**不判优劣、不改正文**。

### 多格式导出（`export`）

```
python pipeline/run.py export 长夜将尽 --format all     # epub + html + txt
python pipeline/run.py export 长夜将尽 --format epub
python pipeline/run.py export 长夜将尽 --keep-anchors   # 保留审校锚点（默认剥离为净稿）
```

### 双语发行（`translate` + `export --lang en`）

```
python pipeline/run.py translate 长夜将尽          # 术语表 → 逐章英译（chapters_en/）
python pipeline/run.py translate 长夜将尽 --only 3 # 仅译第 3 章
python pipeline/run.py export 长夜将尽 --lang en   # 英文版三格式 → dist_en/
```

### 一键发行到 GitHub Releases（`release`）

```
python pipeline/run.py release 长夜将尽 --dry-run          # 本地打包预览
python pipeline/run.py release 长夜将尽 --prefix ChangYe   # 打包 + 创建发行（版本自动递增）
python pipeline/run.py release 长夜将尽 --tag novels-v1.5  # 指定标签（已存在则覆盖更新）
```

要点：附件按 ASCII 前缀命名（`.epub/.html/.txt` + `-EN` 英文版）；说明自动生成（中文简介取净稿 TXT 的【作品简介】，英文取 `blurb_en.md`）；标签已存在时可重入；依赖 `gh` CLI 发布（dry-run 不需要）。

### 灵活分步与区间控制

```
python pipeline/run.py run 长夜将尽 --stages draft --only 1-5   # 仅写 1~5 章
python pipeline/run.py run 长夜将尽 --stages review --only 3    # 仅审第 3 章
python pipeline/run.py run 长夜将尽 --stages revise --force     # 强制修订
python pipeline/run.py run 长夜将尽 --stages outline --force    # 重做大纲
```

### 知识库检索

```
python pipeline/run.py kb 悬念      # 按相关度展示命中段落
python pipeline/run.py kb           # 列出全部知识库文档
```

### 断点续跑

所有阶段均检查产物是否存在：中断后重跑同一命令会**自动跳过已完成部分**（`--force` 可重做）。每章生成后会记录剧情摘要到 `state.json`，供后续章节衔接。

---

## 知识库如何被使用

`pipeline/kb.py` 按阶段映射注入相关模块（多模块动态预算均衡，单阶段上限 1.4~2 万字符，超长文档保头保尾）：

- `concept` ← 01-概论、06-素材与创意、08-质量规则
- `world` ← 01-概论/03、02-世界设定、08-质量规则
- `characters` ← 03-角色、02-世界设定/04
- `outline` ← 04-情节结构、06-素材与创意、01-概论/03
- `draft` ← 08-质量规则、05-文风与叙事、04-情节结构、03-角色/03、02-世界设定/01、07-参考/03
- `review` ← 08-质量规则、07-参考/01（72 条清单）、07-参考/02
- `revise` ← 08-质量规则、05-文风与叙事、04-情节结构
- `continuity` ← 08-质量规则、07-参考/01

`short` 形态额外注入 `09-短篇写作`；`--genre` 或 `kb_modules` 挂载的模块追加到每个阶段。

---

## 配置说明

`config.json`（由 `run.py config` 写入）：

| 字段 | 默认值 | 说明 |
|---|---|---|
| `base_url` | `https://api.openai.com/v1` | 任意 OpenAI 兼容接口根地址 |
| `api_key` | 空 | 也可用环境变量 `TXTPUSH_API_KEY` |
| `model` | `gpt-4o-mini` | 见下方「模型实测建议」 |
| `temperature` | 0.8 | 创作温度 |
| `max_tokens` | 4096 | 单次输出上限（正文按每章字数自动放大） |
| `timeout` / `retries` | 600 / 5 | 秒 / 网络错误·429·5xx 自动重试 |
| `extra_params` | `{}` | 端点扩展参数，如 `{"reasoning_effort": "minimal"}` |

`projects/<名>/project.json`：`title`、`genre`、`keywords`、`premise`、`target_chapters`、`words_per_chapter`、`pov`、`tone`、`audience`、`extra`、`work_type`（`novel`/`short`）、`asset_prefix`、`kb_modules` 等，可直接编辑后 `--force` 重跑对应阶段。

---

## Web 端（可选）

`web/` 是免服务器的 PWA 创作工作台：本地知识库检索、流式生成、浏览器端打包 EPUB/HTML/TXT。

```
python pipeline/bundle_kb.py     # 把 knowledge/ 编译为 web/knowledge_bundle.json
python -m http.server 8000       # 在项目根目录启动，访问 http://localhost:8000/web/
```

推送 `main` 后 `.github/workflows/deploy.yml` 会自动编译知识包并部署到 GitHub Pages；`.github/workflows/tests.yml` 在 push/PR 时跑全量测试。

---

## 运行自动化测试

```
python -m unittest discover tests
```

包含 LLM 客户端容错、知识库加载与题材模块、大纲切分、EPUB 封装、统计与审计、
三族锚点剥离（W/C、日常细节、条目标题 + 病句 fixup + export 端到端）、
双语导出链路、发行打包、文风体检、字数闸门护栏、连续性预检、CLI 参数契约等 **75 项**单元测试。

---

## 模型实测建议

- 推荐非推理大参数模型（如 `deepseek-chat`、`gpt-4o`、`nvidia/nemotron-3-super-120b-a12b`）以获得平稳的中文正文输出速度；
- 推理模型（DeepSeek-R1、GLM-Zero、Kimi 类）已内置 `reasoning_content` 截断防护：思考耗尽时自动加倍 `max_tokens`（上限 32000）并安全重试；
- **换模型前先横测**：`python benchmark_models.py`（延迟 + 中文创作质量双维度）；
- ⚠️ NVIDIA 端点按账号开通模型：返回 `Function … Not found for account`（404）说明该账号未开通；
- PowerShell 5.1 直接读取 UTF-8 中文可能显示乱码，用 `Get-Content -Encoding utf8`、VS Code 或 `chcp 65001` 查看（流水线自身读写不受影响）。

---

## 注意事项

- `config.json` 含 API Key（已 gitignore），仓库只保留 `config.example.json`；
- 真实创作建议：先人工审阅 `00-创作概念.md` 与 `03-大纲.md`（改完再用 `--force` 推进后续阶段），再批量写正文，然后走完整审校链，最后 `assemble` 成书导出；
- 发行附件名必须 ASCII（`asset_prefix` 用拼音），否则会被 GitHub 静默剥离为 `default.epub`；
- 知识库文档可直接当写作参考，或复制其中的提示词手工使用。
