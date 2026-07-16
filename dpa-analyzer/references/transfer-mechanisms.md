# International Transfer Mechanisms

Guidance for Step 5 of the DPA Analyzer. Always verify current status before relying on this file — use web search for DPF and SCC currency.

---

## Decision tree

```
Is data leaving the EEA?
│
├─ No → No transfer mechanism needed. ✅
│
└─ Yes → What country?
         │
         ├─ Adequacy decision in force? → ✅ (note if adequacy is under review)
         │
         ├─ US → Is vendor DPF-certified for this processing? → ✅ (flag Schrems III ⓘ)
         │
         └─ No adequacy, no DPF → SCCs required
                                   │
                                   └─ Which module?
                                      M1: C→C, M2: C→P (most common), M3: P→P, M4: P→C
```

---

## Adequacy decisions (as of knowledge cutoff — always verify)

| Country / Territory | Status |
|---|---|
| UK | Adequacy (post-Brexit; subject to renewal) |
| Switzerland | Adequacy |
| Japan | Adequacy |
| South Korea | Adequacy |
| Canada (PIPEDA-covered commercial orgs) | Adequacy |
| Israel | Adequacy |
| New Zealand | Adequacy |
| Argentina | Adequacy |
| Andorra, Faroe Islands, Guernsey, Isle of Man, Jersey | Adequacy |
| US | No general adequacy — DPF only for certified orgs |
| India, Brazil, Australia, UAE, China | No adequacy |

**Verification required:** Adequacy status can be revoked (UK adequacy subject to review; Schrems III pending for DPF). Always web-search before relying on this table.

---

## EU-US Data Privacy Framework (DPF)

- Replaces Privacy Shield (invalidated by Schrems II, July 2020)
- Valid for certified organisations — check https://www.dataprivacyframework.gov/
- Subject to ongoing Schrems III challenge — flag as ⓘ INFORMATIONAL: stable for now but politically fragile

How to verify certification:
1. Check vendor's DPF certification at dataprivacyframework.gov (search by org name)
2. Confirm scope covers the data types in question (HR data vs. commercial data — DPF has separate HR principles)
3. Confirm certification is current (not expired)

If DPF is the sole transfer mechanism and vendor is not certified → 🔴.

---

## Standard Contractual Clauses (SCCs)

Current version: **Commission Decision 2021/914** (in force since 27 June 2021; mandatory since 27 December 2022).
Old 2010 SCCs: **INVALID** since 27 December 2022 → 🔴 if found in DPA.

### SCC Modules

| Module | Use case | Most common in |
|---|---|---|
| Module 1 | Controller → Controller | Two independent companies exchanging personal data |
| Module 2 | Controller → Processor | **Most SaaS DPAs** — buyer (controller) → vendor (processor) |
| Module 3 | Processor → Processor | Vendor → sub-processor chain |
| Module 4 | Processor → Controller | Rare (e.g., processor returns data to controller in third country) |

**Wrong module = structural gap:**
- Module 1 used where Module 2 should apply → 🟠 (omits instruction principle, different data subject rights)
- No module specified, just "SCCs apply" → 🟠 (ambiguous; push to name the module)

### SCC in-scope checks

Even if correct module is selected, verify:
- Annex I (parties, description of transfer) is filled in, not blank → 🟠 if blank
- Annex II (TOMs) is filled in, not "see Security Policy" with no link → 🟠
- Annex III (list of sub-processors, for Module 2) is populated → 🟠 if blank
- Governing law of SCCs is specified (must be an EU Member State)
- Local law assessment (Transfer Impact Assessment) referenced or conducted

---

## Transfer Impact Assessment (TIA)

Not legally mandatory but EDPB-recommended (Guidelines 05/2021) and best practice after Schrems II.

| Found | Severity |
|---|---|
| TIA conducted and documented, available on request | 🟢 |
| TIA referenced in DPA, not attached | 🟢 (request copy) |
| No TIA but SCCs + DPF in place for low-sensitivity data | 🟢 (ⓘ flag) |
| No TIA, SCCs only, US vendor, high-sensitivity data (financial, health) | 🟠 — recommend buyer conduct its own TIA |
| No TIA, no SCCs, just "we comply with applicable law" | 🔴 |

Simplified TIA checklist for buyer's reference (note in comment):
1. What surveillance/access laws apply in the destination country?
2. Has the vendor received any government access orders in the past 12 months?
3. Does the vendor's transparency report disclose government access requests?
4. Are TOMs sufficient to render data inaccessible to authorities (e.g., end-to-end encryption with keys held by controller)?

---

## Poland-specific: UODO guidance on transfers

- UODO aligns with EDPB position on Schrems II
- UODO has issued enforcement decisions on inadequate transfer mechanisms
- For transfers to the US: UODO has not objected to DPF-based transfers, but has flagged risks in its guidance
- Polish entities are subject to UODO enforcement — a defective transfer mechanism exposes the buyer (controller) directly, not just the vendor

Always note in the comment: "Jako administrator, Państwa Spółka ponosi bezpośrednią odpowiedzialność przed UODO za zgodność mechanizmu transferu z RODO."
