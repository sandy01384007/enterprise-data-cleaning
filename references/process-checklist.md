# Enterprise Data Cleaning — Process & Department Checklists

## Universal 7-Step Checklist

- [ ] 1. Inventory completed (file list + size + date + suggested domain + hash)
- [ ] 2. Duplicates removed (keep latest / most complete)
- [ ] 3. Format converted to searchable text or structured tables (OCR done for scans)
- [ ] 4. Desensitization applied and **manually reviewed**
- [ ] 5. Naming convention applied + full metadata filled
- [ ] 6. Content cleaned (headers, garbage, terminology normalized)
- [ ] 7. Owner sign-off + permission level set + ready for ingest

## Design / Engineering Checklist

- [ ] Drawings have extracted text notes / parameter tables
- [ ] Units and equipment names normalized
- [ ] Cases include location, scale, key brands, lessons
- [ ] Real client names replaced
- [ ] Metadata complete (location, scale, brands)
- [ ] Permission usually `internal`

## Finance Checklist

- [ ] Only templates / structures / non-sensitive analysis submitted to shared KB
- [ ] All real amounts replaced or kept in confidential store
- [ ] Counterparty names coded or removed
- [ ] `permission_level = confidential`
- [ ] Finance owner signed off

## HR Checklist

- [ ] Latest policy versions only
- [ ] No names, ID numbers, phones, exact salaries, scores
- [ ] Certificates aggregated for bidding use
- [ ] Training materials cleaned of personal data
- [ ] HR owner signed off

## Admin Checklist

- [ ] Only current valid versions retained
- [ ] Naming + version numbers consistent
- [ ] Effective date and applicable departments filled
- [ ] Admin owner signed off

## Bidding / Sales Checklist

- [ ] Client names, exact prices, internal strategy removed
- [ ] Reusable templates extracted (commercial / technical / deviation / performance)
- [ ] Tagged by project type and region
- [ ] Permission appropriate (templates `internal`, sensitive parts `restricted`)
- [ ] Owner signed off

## Cost Estimation Checklist

- [ ] Prices stored as ranges + time + brand/model
- [ ] Absolute transaction values masked
- [ ] Cost structure logic retained
- [ ] Local market notes (tax/freight/labor) captured if useful
- [ ] Permission `restricted` or `confidential` for price data
- [ ] Owner signed off

## Quick Self-Check Before Handover (Interface Person)

1. Correct domain classification?
2. No duplicates left?
3. Searchable text available?
4. Sensitive data thoroughly masked?
5. All required metadata present?
6. Naming convention followed?
7. Permission level correct?
8. Terminology aligned with company glossary?
9. Department owner confirmed?
10. Submitted to knowledge-base owner for final check?
