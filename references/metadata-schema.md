# Metadata Schema (Enterprise Knowledge Base)

## Core Required Fields

| Field (EN) | Field (ZH) | Type | Required | Example |
|------------|------------|------|----------|---------|
| doc_id | 文档唯一ID | string | Yes (auto or rule) | BD-TPL-2025-003 |
| title | 标题 | string | Yes | 储能EPC商务标模板 |
| domain | 一级知识域 | enum | Yes | 商务数据库 |
| sub_domain | 二级分类 | enum | Yes | 招投标模板 |
| doc_type | 文件类型 | enum | Yes | template |
| language | 语言 | enum | Yes | zh-CN |
| permission_level | 权限等级 | enum | Yes | internal |
| tags | 标签 | multi | Yes | 储能,EPC,投标,模板 |
| summary | 摘要 | text | Yes | 标准商务标结构与常见条款 |
| owner | 责任人 | string | Yes | 李四 |
| status | 状态 | enum | Yes | active |
| created_date | 创建日期 | date | Yes | 2025-06-15 |
| upload_date | 入库日期 | date | Yes | 2026-03-01 |

## Strongly Recommended / Conditional

| Field | When to use | Example |
|-------|-------------|---------| 
| project_location | Projects / cases | 越南-平阳省 |
| capacity_or_scale | Energy / construction | 5.0 (MW) |
| equipment_brand | Technical docs | 华为,阳光 |
| standard_code | Standards | TCVN / GB/T 19964 |
| version | All | v2.1 |
| related_ids | Linked documents | PV-CASE-2024-012 |
| vietnam_specific / region_flag | Multi-country ops | true |

## Permission Enum

- public
- internal
- restricted
- confidential

## Status Enum

- active
- expired
- draft
- archived

## Naming Pattern

`[DOMAIN]-[TYPE]-[YEAR]-[SEQ]-[short-title].[ext]`

Domain examples: PV, ST, PD, BD, FIN, HR, ADM, COST, LEG, GEN, TECH, ENG  
Type examples: CASE, SPEC, STD, TPL, POL, RPT, DWG, SCH
