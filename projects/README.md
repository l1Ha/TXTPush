# projects/ —— 每部小说一个独立工作区

本目录存放流水线生成的小说项目。创建方式：

```
python pipeline/run.py init <项目名> --genre <题材> --keywords ... --premise ...
```

单个项目目录结构：

```
<项目名>/
├── project.json        # 书名、题材、关键词、章数、字数、视角等（可直接编辑）
├── state.json          # 阶段状态、逐章摘要、Token 用量（断点续跑）
├── 00-创作概念.md      # concept 阶段产物
├── 01-世界设定.md      # world 阶段产物
├── 02-角色.md          # characters 阶段产物
├── 03-大纲.md          # outline 阶段产物
├── chapters/           # 逐章正文（修订产生 .bak 备份，已被 gitignore）
├── reviews/            # 逐章审校报告、连续性报告、文风体检报告
├── manuscript/         # 汇编成书稿
├── dist/               # 中文出版交付物（epub/html/txt）
├── chapters_en/        # 英文译稿（translate 支线）
├── glossary_en.md      # 中英术语对照表
├── blurb_en.md         # 英文版简介
└── dist_en/            # 英文出版交付物
```
