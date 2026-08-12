---
name: enterprise-data-cleaning
description: Enterprise data cleaning for AI knowledge bases and RAG. Use when the user asks to clean, desensitize, structure, inventory, rename, or prepare documents for a knowledge base, RAG system, or AI agents. Covers multi-department data (design, finance, HR, admin, bidding, cost, sales, legal), metadata standards, PII redaction, file naming, vectorization prep, and department checklists. Triggers include data cleaning, 数据清洗, desensitize, 脱敏, document inventory, metadata template, knowledge base preparation, RAG data prep.
---

# Enterprise Data Cleaning

Prepare enterprise documents for AI knowledge bases and RAG systems. Focus on safety (desensitization), structure (metadata + naming), and retrievability.

## Core Principles

1. Safety first — never put real customer names, contract amounts, ID numbers, salaries, or internal costs into a shared/public knowledge base.
2. Quality over quantity — fewer clean, well-tagged documents beat many messy ones.
3. Standardize early — enforce naming and metadata before vectorization.
4. Human-in-the-loop — scripts assist; final review and sensitive decisions stay with domain owners.

## Standard 7-Step Process

Always guide the user through these steps (adapt order if needed):

1. **Inventory** — Scan folders, list files, detect likely duplicates (hash), suggest domain.
2. **Deduplicate** — Keep newest/most complete version only.
3. **Format conversion** — PDF/Word/Excel/CAD notes → searchable text or structured tables. OCR scanned pages.
4. **Desensitize** — Replace PII and sensitive business data with placeholders.
5. **Standardize + Metadata** — Apply naming convention and fill required metadata fields.
6. **Content clean** — Remove headers/footers, garbage, normalize terminology.
7. **QA + Ingest** — Spot-check, owner sign-off, then load into knowledge base / vector store.

## Required Metadata Fields

Every document must carry at least:

| Field | Required | Notes |
|-------|----------|-------|
| title | Yes | Clear Chinese or English title |
| domain | Yes | Top-level knowledge domain |
| sub_domain | Yes | Second-level category |
| doc_type | Yes | case / spec / standard / template / policy / drawing-note / other |
| language | Yes | zh-CN / en / vi / multi / other |
| permission_level | Yes | public / internal / restricted / confidential |
| tags | Yes | Comma-separated keywords |
| summary | Yes | ≤100 characters |
| owner | Yes | Content maintainer |
| status | Yes | active / expired / draft |
| created_date / upload_date | Yes | ISO dates |
| project_location | Strongly recommended | Country-province or equivalent |
| capacity_or_scale | When applicable | e.g. MW, MWh, headcount |
| version | Recommended | |

Permission levels:
- `public` — OK for broad access
- `internal` — company staff
- `restricted` — named roles only
- `confidential` — finance / HR / senior management only (contracts, salaries, exact prices)

## File Naming Convention

```
[DOMAIN]-[TYPE]-[YEAR]-[SEQ]-[short-title].[ext]
```

Domain codes (customize per company):
- PV / TECH / ENG — technical / design
- FIN — finance
- HR — human resources
- ADM — admin / policy
- BD / SALES — commercial / bidding
- COST — cost estimation
- LEG — legal
- GEN — general / company

Type codes: CASE, SPEC, STD, TPL, POL, RPT, DWG, SCH

Example: `BD-TPL-2025-003-储能EPC商务标模板.docx`

## Department-Specific Guidance

### Design / Engineering
- Extract text descriptions and parameter tables from drawings; do not rely on raw CAD alone.
- Normalize units and equipment names.
- Case studies must include location, scale, key equipment, lessons learned.
- Desensitize real client names → “Project A – Industrial Park Rooftop”.

### Finance
- Prefer templates, chart-of-accounts structure, and analysis logic only.
- Real amounts and counterparty names → placeholders or stay in confidential store.
- Always set `permission_level = confidential` for anything with numbers.

### HR
- Policies can stay; remove names, ID numbers, phone numbers, exact salaries, performance scores.
- Certificates for bidding → aggregated counts (“X people hold Y certificate”), never individual details.

### Admin
- Keep only the latest valid version of policies and process docs.
- Add effective date and applicable departments.

### Bidding / Sales
- High value. Strip client names, exact bid prices, internal margin strategy.
- Extract reusable templates (commercial structure, technical structure, deviation table, performance summary).
- Tag by project type and region.

### Cost Estimation
- Store price ranges + time + brand/model, not exact transaction prices.
- Keep cost-structure logic; mask absolute numbers.
- Local market notes (tax, freight, labor) are valuable and usually safe.

## Desensitization Rules (Baseline)

Replace with clear placeholders:
- Chinese ID (18-digit) → 【身份证号】
- Mobile numbers → 【手机号】
- Email → 【邮箱】
- Bank card-like long digit sequences → 【银行卡号】
- Currency amounts (¥ / 人民币 / 元) → 【金额】
- Real company/client names (context-dependent) → 【客户A】 or project code

Scripts can handle the pattern-based items; names and business context require human review.

## Vectorization Prep Notes

- Chunk by semantic units or headings (400–800 tokens, 50–100 overlap typical).
- Inject full metadata into every chunk payload so retrieval can filter by domain, location, permission.
- Use the same multilingual embedding model for the whole corpus.
- Keep confidential collections separate or heavily filtered at query time.
- Always return source chunks with answers.

## Recommended Tooling Path

1. Inventory + basic rename + metadata template (scripts in this skill).
2. PDF → text (pypdf or commercial OCR for scans).
3. Regex desensitization + manual review.
4. Notion / Excel for metadata staging → vector DB (Qdrant / Chroma / Milvus etc.).

## Using Bundled Resources

- `scripts/` — ready-to-run Python helpers (inventory, rename, desensitize, PDF-to-text, metadata template). Copy or adapt them for the user’s environment.
- `references/process-checklist.md` — full process + per-department checklists.
- `references/metadata-schema.md` — detailed field definitions.
- `assets/` — optional empty templates if needed.

When the user asks for a complete cleaning run, start with inventory, then propose the department-specific checklist, then offer the relevant script.

## Output Expectations

- Always produce concrete, copy-pasteable checklists or command examples.
- Warn clearly that automated desensitization is incomplete and requires human sign-off.
- For highly regulated data (finance, HR, personal data), default to “manual only + confidential store”.
- Prefer generating Excel/CSV templates or Word manuals the team can fill and track.
