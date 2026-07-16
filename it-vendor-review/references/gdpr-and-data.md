# GDPR and Data Protection Checks

Apply whenever the vendor processes, stores, or accesses **any personal data** of buyer's employees, customers, or other EU data subjects.

---

## 1. DPA Existence (GDPR Article 28)

**Flag:**
- No DPA (Data Processing Agreement) despite personal data being processed: 🔴 CRITICAL — Art. 28 GDPR violation. Buyer as controller is liable.
- DPA is a separate document not signed/countersigned: 🟡 MEDIUM — verify it's properly executed.
- DPA is incorporated by reference to vendor's website ("as updated from time to time"): 🔴 CRITICAL — unilateral changes to a legally required agreement.

---

## 2. DPA Content — Required Under Art. 28(3) GDPR

Each item below must be explicitly addressed:

| Requirement | If absent |
|---|---|
| Subject matter, duration, nature and purpose of processing | 🟠 HIGH |
| Type of personal data and categories of data subjects | 🟠 HIGH |
| Processing only on documented buyer instructions | 🔴 CRITICAL |
| Confidentiality obligation on vendor's staff | 🟠 HIGH |
| Security measures (Art. 32 GDPR) | 🔴 CRITICAL |
| Sub-processor rules (prior written consent or general authorization + notification) | 🟠 HIGH |
| Assistance with data subject rights (access, erasure, portability) | 🟠 HIGH |
| Assistance with Art. 32–36 obligations (security, DPIA, breach notification) | 🟠 HIGH |
| Data deletion or return at contract end | 🔴 CRITICAL |
| Audit / inspection cooperation right for buyer | 🟠 HIGH |

---

## 3. Cross-Border Data Transfers

**Flag:**
- Data processed or stored outside EEA without a transfer mechanism: 🔴 CRITICAL.
- Transfer mechanism claimed: verify it is valid:
  - EU-US Data Privacy Framework (DPF) — check vendor is certified at [privacyshield.gov](https://www.privacyshield.gov) (search within session if needed)
  - SCCs (Standard Contractual Clauses) — must be 2021 version (Decision 2021/914). Old 2010 SCCs are invalid: 🔴 CRITICAL.
  - BCRs — verify approved by a lead DPA.
  - Adequacy decision — check status for the specific country.
- Vendor processes data in US but relies on DPF — verify vendor is actually listed on DPF registry.
- Transfer impact assessment (TIA) for high-risk transfers — absent: 🟠 HIGH.
- Data residency option — can buyer elect EU-only storage? If not available: 🟠 HIGH for regulated or sensitive data.

---

## 4. Data Breach Notification

**Flag:**
- Breach notification timeline > 72 hours: 🔴 CRITICAL — GDPR requires controller to notify DPA (UODO in Poland) within 72 hours of becoming aware.
- Notification obligation is on buyer, but vendor is not required to notify buyer immediately: 🔴 CRITICAL — vendor must notify buyer "without undue delay" (interpretive: ≤ 24–48 hours).
- "Material breach" threshold — vendor only notifies if breach is "material": 🔴 CRITICAL — any breach affecting personal data must be notified.
- Notification content not specified — vendor can provide minimal information: 🟠 HIGH.
- Vendor not required to assist buyer in notifying affected data subjects: 🟠 HIGH.

---

## 5. Sub-processors

**Flag:**
- No list of sub-processors disclosed: 🟠 HIGH.
- No prior consent / notification required for adding new sub-processors: 🟠 HIGH. Push for: general authorization with 30-day advance notice and right to object.
- Sub-processor list only available on vendor's website ("as updated") — no contractual freeze: 🟠 HIGH.
- Sub-processors in non-adequate countries without documented transfer mechanism: 🔴 CRITICAL.

---

## 6. Data Retention and Deletion

**Flag:**
- Retention period not specified — "as long as necessary": 🟠 HIGH. Require specific periods.
- No deletion obligation at contract end: 🟠 HIGH.
- No confirmation of deletion in writing: 🟡 MEDIUM.
- Backup copies excluded from deletion obligation: 🟠 HIGH.
- Retention for vendor's own analytics purposes beyond contract term: 🟠 HIGH.
- "We may retain data to comply with legal obligations" — without specifying which obligations or time limit: 🟡 MEDIUM.

---

## 7. AI Training on Buyer's Data

**Flag (emerging critical issue for AI/LLM vendors):**
- Vendor uses buyer's data (including personal data) to train or improve AI models: 🔴 CRITICAL — this likely exceeds processing permitted under Art. 28(3)(a) and requires separate legal basis.
- Opt-out exists but is not the default: 🟠 HIGH. Require opt-in, not opt-out.
- "Aggregated and anonymized data" used for training — verify actual anonymization standard (Art. 29 WP / EDPB Opinion 05/2014): 🟡 MEDIUM.

---

## 8. Security Certifications

**Minimum expected for B2B SaaS processing personal data:**

| Certification | Verdict if absent |
|---|---|
| ISO 27001 or SOC 2 Type II | 🟠 HIGH for any personal data processing |
| ISO 27701 (Privacy) or equivalent | 🟡 MEDIUM |
| DORA compliance (if financial sector) | 🔴 CRITICAL for financial sector buyers |
| NIS2 compliance (if critical infrastructure) | 🔴 CRITICAL if applicable |

- Certifications referenced but no obligation to maintain them: 🟡 MEDIUM.
- Certifications not required to cover the specific services/infrastructure buyer uses: 🟡 MEDIUM.
