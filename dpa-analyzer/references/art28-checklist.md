# GDPR Art. 28(3) — Annotated Mandatory Elements Checklist

Every DPA must contain all of these. Missing element = finding. Use this as the backbone of Step 3.

---

## Element 1 — Subject matter, nature, duration, purpose of processing

**Art. 28(3) preamble**

| Quality | Severity |
|---|---|
| Specific: named service, named purposes, defined term (start + end or "for term of main agreement") | 🟢 |
| Generic: "processing necessary to provide the Services" | 🟠 |
| Absent entirely | 🔴 |

Suggested language:
> "The subject matter of the Processing is the provision of [Service Name] to Customer. The nature of the Processing is [describe: storage, analysis, transmission, etc.]. The purpose of the Processing is [describe]. The duration of the Processing is the term of the Agreement plus any post-termination data retention period specified herein."

---

## Element 2 — Type of personal data and categories of data subjects

**Art. 28(3) preamble + Annex obligation**

This should be in an Annex (Załącznik), not just the body. Vague schedule = weak DPA.

| Quality | Severity |
|---|---|
| Annex lists specific data categories and data subject categories | 🟢 |
| "Data as uploaded by Customer" or "as described in the Order Form" | 🟠 — push for specificity |
| No Annex / no description | 🟠 → 🔴 if special categories likely |

**Special categories (Art. 9):** If the use case involves health, biometric, financial (in context of creditworthiness), or children's data — the DPA **must** name them. Silence on Art. 9 data = 🔴.

**Context-specific (financial forecasts):** If financial budget/forecast data is processed, flag that while not Art. 9, it constitutes business confidential data with high sensitivity — the DPA should explicitly acknowledge this category and vendor's restrictions on use.

Suggested annex language:
> "Categories of data subjects: [e.g., employees of Customer and its Affiliates; customers of Customer; business partners of Customer]. Categories of personal data: [e.g., name, contact details, job title, authentication credentials, [financial data where applicable]]. Special categories (Art. 9): [none / describe]. Approximate volume: [X data subjects]."

---

## Element 3 — Processor acts only on documented instructions

**Art. 28(3)(a)**

Core principle: vendor can only process data as instructed by the controller.

| Quality | Severity |
|---|---|
| Explicit obligation + carve-out only for legal requirement (with notification obligation) | 🟢 |
| Present but no legal-requirement carve-out | 🟠 |
| "Processor may process data as necessary for legitimate interests" or similar | 🔴 — violates the instruction principle |
| Absent | 🔴 |

Also check: does the instruction principle cover **all processing**, including training/analytics? Many AI vendor DPAs carve out model improvement from the instruction principle. This is 🔴 if buyer's data is used for model training without explicit opt-in.

Suggested language:
> "Processor shall process Personal Data only on documented instructions from Controller, including with regard to transfers to third countries, unless required to do so by Union or Member State law to which Processor is subject; in such a case, Processor shall inform Controller of that legal requirement before processing, unless that law prohibits such information."

---

## Element 4 — Confidentiality obligations on processor's staff

**Art. 28(3)(b)**

| Quality | Severity |
|---|---|
| Explicit obligation + limited to authorised personnel + ongoing after employment | 🟢 |
| "Staff with need to know" — no post-employment survival | 🟠 |
| Absent | 🟠 |

---

## Element 5 — Security measures (Art. 32)

**Art. 28(3)(c)**

See also TOMs analysis in Step 6 of the main skill.

| Quality | Severity |
|---|---|
| Specific TOMs in Annex: encryption, pseudonymisation, access control, testing, incident response | 🟢 |
| ISO 27001 / SOC 2 Type II certification referenced + made available on request | 🟢 |
| "Appropriate technical and organisational measures" — no specifics | 🟠 |
| Nothing | 🔴 |

For special categories or financial data: minimum bar should include:
- Encryption at rest (AES-256 or equivalent) ✓/✗
- Encryption in transit (TLS 1.2+) ✓/✗
- Access controls + MFA for privileged access ✓/✗
- Annual pen testing or vulnerability scanning ✓/✗

---

## Element 6 — Sub-processor authorisation

**Art. 28(3)(d) + Art. 28(2)**

See full analysis in `subprocessor-analysis.md`. Summary:

| Found | Severity |
|---|---|
| General written authorisation + list + 30-day notice + right to object with exit right | 🟢 |
| General authorisation + notice, but notice < 10 days or no exit right | 🟠 |
| Vendor may change sub-processors at will | 🔴 |
| No sub-processor provision at all | 🔴 |

---

## Element 7 — Assistance with data subject rights

**Art. 28(3)(e)**

| Found | Severity |
|---|---|
| Obligation present + SLA (≤ 5 business days) + all GDPR rights covered | 🟢 |
| Obligation present, "reasonable assistance", no SLA | 🟠 |
| Covers only some rights (e.g., erasure only) | 🟠 |
| Absent | 🔴 |

Note: Art. 17 erasure right carries extra weight — if vendor provides AI/analytics, erasure from derived artefacts must also be addressed.

---

## Element 8 — Assistance with Art. 32–36 obligations

**Art. 28(3)(f)**

Four sub-obligations:
1. Art. 32 — security (→ TOMs, covered separately)
2. Art. 33–34 — breach notification (→ covered in Step 8 of main skill)
3. Art. 35 — DPIA assistance
4. Art. 36 — prior consultation assistance

| Found | Severity |
|---|---|
| All four addressed | 🟢 |
| Only breach notification, TOMs absent or silent on DPIA/prior consultation | 🟠 |
| Only "we comply with applicable law" | 🟠 |
| Absent | 🔴 |

**DPIA note:** If the vendor's service involves systematic large-scale processing, profiling, or AI-based decision-making, buyer may be required to conduct a DPIA (Art. 35). Vendor should contractually commit to assist. Flag if absent and use case is AI-based or large-scale.

---

## Element 9 — Return or deletion of data

**Art. 28(3)(g)**

See Step 10 of main skill.

| Found | Severity |
|---|---|
| Return or deletion at buyer's choice + certificate + deadline (≤ 90 days) | 🟢 |
| Deletion only, no return option | 🟠 |
| Deletion timeline > 180 days | 🟠 |
| "Deletion per vendor's standard schedule" | 🟠 |
| Absent | 🔴 |

---

## Element 10 — Audit rights

**Art. 28(3)(h)**

See Step 9 of main skill.

| Found | Severity |
|---|---|
| On-site audit right (with notice) + third-party audit reports on request | 🟢 |
| Audit report access only (SOC 2, ISO 27001) — no on-site | 🟠 (borderline acceptable for cloud SaaS) |
| Questionnaire only | 🟠 |
| Absent | 🔴 |

---

## Art. 28(3) Quick Summary Table

Use this to populate the executive summary checklist:

| # | Element | ✅/❌/⚠️ | Default severity if missing |
|---|---|---|---|
| 1 | Subject matter / nature / duration / purpose | | 🔴 |
| 2 | Data categories + data subjects Annex | | 🟠–🔴 |
| 3 | Instruction principle | | 🔴 |
| 4 | Staff confidentiality | | 🟠 |
| 5 | Security / TOMs (Art. 32) | | 🔴 |
| 6 | Sub-processor authorisation | | 🔴 |
| 7 | DSR assistance | | 🔴 |
| 8 | Art. 32–36 assistance (breach, DPIA, consultation) | | 🟠–🔴 |
| 9 | Data return / deletion | | 🔴 |
| 10 | Audit rights | | 🔴 |
