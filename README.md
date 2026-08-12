# Enterprise Data Cleaning Skill

企业级 AI 知识库 / RAG 数据清洗 Skill。

适用于所有企业在建设 AI 知识库、RAG 系统或专业 Agent 前，对设计、财务、人事、行政、投标、造价等部门资料进行标准化清洗、脱敏、元数据标注与入库准备。

## 快速开始

将本仓库内容放入你的 Skills 目录（例如 `.grok/skills/enterprise-data-cleaning/`），即可被支持 Skills 的 Agent 自动加载。

### 触发词示例

- 数据清洗 / 脱敏
- knowledge base preparation / RAG data prep
- 文件盘点、批量重命名、元数据模板
- 各部门数据整理检查表

## 目录结构

```
enterprise-data-cleaning/
├── SKILL.md                          # Skill 主指令
├── scripts/                          # 可运行的 Python 自动化脚本
│   ├── 01_file_inventory.py
│   ├── 02_batch_rename.py
│   ├── 03_desensitize_text.py
│   ├── 04_pdf_to_text.py
│   ├── 05_generate_metadata_template.py
│   └── README.md
├── references/
│   ├── process-checklist.md          # 完整流程 + 各部门检查表
│   └── metadata-schema.md            # 元数据字段定义
└── assets/
```

## 脚本依赖

```bash
pip install pypdf python-docx openpyxl pandas
```

## 核心能力

1. 标准七步清洗流程
2. 多部门专项要求（设计 / 财务 / 人事 / 行政 / 投标 / 造价）
3. 统一元数据规范与文件命名规范
4. PII 与敏感业务数据脱敏规则
5. 向量化（RAG）准备建议
6. 可直接运行的自动化脚本

## License

MIT（可按需修改）
