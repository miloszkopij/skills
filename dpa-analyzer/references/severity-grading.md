# Severity Grading — Context-Based Re-grading Rules

Default severities are set in the checklists. This file governs how to **shift** them based on use-case context captured in Step 0.5.

---

## Re-grading matrix

### By data type

| Finding | Default | Special categories (Art. 9) | Financial data / forecasts | Employee HR only | Public/non-sensitive |
|---|---|---|---|---|---|
| Vague TOMs ("industry standard") | 🟠 | 🔴 | 🔴 | 🟠 | 🟠 |
| No TIA for US transfer | 🟠 | 🔴 | 🔴 | 🟠 | ⓘ |
| Missing data categories Annex | 🟠 | 🔴 | 🟠 | 🟠 | 🟠 |
| Sub-processor notice < 14 days | 🟠 | 🔴 | 🟠 | 🟠 | 🟠 |
| Breach notification "promptly" | 🟠 | 🔴 | 🔴 | 🟠 | 🟠 |
| Model training not excluded | 🟠 | 🔴 | 🔴 | 🟠 | 🟠 |
| Audit reports only (no on-site) | 🟠 | 🟠 | 🟠 | 🟢 | 🟢 |

### By use case

| Finding | Internal employee tool | Customer-facing | Agentic/automated | B2B partner data |
|---|---|---|---|---|
| No DPIA assistance clause | ⓘ | 🟠 | 🟠 | ⓘ |
| High-Risk AI system (AI Act Annex III) unacknowledged | 🟠 | 🔴 | 🔴 | 🟠 |
| DSR assistance — "reasonable efforts" only | 🟠 | 🔴 | 🔴 | 🟠 |
| No data portability / export | 🟠 | 🟠 | 🟠 | ⓘ |
| Liability cap 6 months | 🟠 | 🔴 | 🔴 | 🟠 |

### By criticality

| Finding | POC / pilot | Production non-critical | Production critical |
|---|---|---|---|
| No SLA / availability commitment | ⓘ | 🟠 | 🔴 |
| Vendor suspension "at sole discretion" | ⓘ | 🟠 | 🔴 |
| Short data return window (< 15 days post-term) | ⓘ | 🟠 | 🟠 |
| Liability cap 6 months | 🟢 | 🟠 | 🔴 |
| No audit rights | 🟠 | 🟠 | 🟠 → 🔴 if regulated sector |

---

## Multi-entity re-grading

If **multiple supporting entities are co-controllers** and DPA doesn't cover them:

| Finding | Only main entity affected | All group entities affected |
|---|---|---|
| DPA silent on Affiliates | 🟠 | 🔴 |
| Sub-processor list doesn't cover all group flows | 🟠 | 🔴 |
| No Art. 26 arrangement between entities | ⓘ | 🟠 |

---

## Financial data — special rules

When financial forecasts, budgets, or financial models are in scope:

1. **Flag proactively** — don't wait for the user to note it. Ask in Step 0.5.
2. Even if not Art. 9 special categories, financial data is typically covered by trade-secret protections and sometimes by financial regulation (banking secrecy, if applicable).
3. Push for:
   - Explicit "Confidential Information" classification in the DPA's data categories Annex
   - Restrictions on vendor analytics use of financial data
   - Deletion of derived analytics within the same timeline as raw data
4. If the vendor is a SaaS analytics/forecasting platform (e.g., financial planning software):
   - Model training on customer financial data = 🔴 regardless of other context
   - Benchmarking / anonymised aggregation use = 🟠 (needs explicit opt-out)

---

## How to apply re-grading in practice

1. Start with the checklist default severity.
2. Look up the finding in the relevant re-grading table.
3. Apply the highest severity from any applicable column (data type OR use case OR criticality).
4. Document the re-grading reason in the comment: "Dla Państwa zastosowania ([use case]) i kategorii danych ([data type]) ustala się wyższy poziom ryzyka niż domyślny..."
5. Reflect the final severity in the executive summary count.

---

## Absences that only surface from context

These are findings with no default because they only exist when context makes them relevant:

| Context | Absence to flag | Severity |
|---|---|---|
| Production-critical use, no SLA | Missing SLA provision | 🔴 |
| Customer-facing chatbot, no AI Act disclosure | Missing AI Act Art. 13/14 compliance clause | 🟠 |
| Fine-tuning / model training, no explicit prohibition | Missing model training restriction | 🔴 |
| Multiple group entities, no Art. 26 arrangement | Missing joint-controller arrangement | 🟠 |
| Financial data in scope, no confidentiality Annex | Missing financial data classification | 🟠 |
| DPIA likely needed (systematic/large-scale), no DPIA assistance | Missing Art. 35 assistance clause | 🟠 |
| Special categories (Art. 9) in scope, no explicit mention | Missing Art. 9 acknowledgement | 🔴 |
