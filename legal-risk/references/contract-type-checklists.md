# Contract-Type-Specific Checklists

Each section is a checklist for a specific contract type. Skim the one(s) that apply, in addition to the EU/Poland and IP/licensing checklists which always apply.

---

## Terms of Service / T&C / EULA / SaaS Agreement

### Things that must be present
- [ ] Clear description of the service / what's included
- [ ] Service Level Agreement (SLA) or commitment to availability (if it's production-relevant)
- [ ] Data handling commitments (link to DPA)
- [ ] Pricing — at minimum a reference to a pricing page or order form
- [ ] Term and termination provisions
- [ ] Liability cap
- [ ] Governing law and dispute resolution

### Red flags specific to T&C
- "Anthropic may update these Terms at any time" with no notice or only short notice → 🟠 NEGOTIATE if it's a unilateral change (consider locking critical terms via order form).
- "Customer agrees to receive marketing communications" with no opt-out → 🟠 — also potentially violates EU ePrivacy.
- Service may be modified or discontinued at any time without compensation → 🟠 NEGOTIATE for production-critical services.
- "Customer is solely responsible for all activity under its account" without security obligations on vendor side → 🟠 NEGOTIATE.
- AI-specific: vendor claims rights to use outputs / inputs for any purpose → see IP reference.
- Reverse-engineering / competition restrictions (very common; usually 🟢 but worth flagging if buyer might build something adjacent).

### Common dark patterns
- Embedding key terms in linked policies that can change independently. Flag this — many incorporated policies = many surfaces vendor can change unilaterally.
- "By accessing the service you agree" without affirmative acceptance step. ⓘ INFORMATIONAL but note enforceability is weaker.
- One-sided choice-of-law clauses (vendor's home jurisdiction, e.g., California).

### SaaS-specific must-haves
- Data export / portability before termination (typically 30–90 days post-termination)
- Backup and disaster recovery commitments
- Security audit reports (SOC 2 / ISO 27001) referenced
- Sub-processor list and update mechanism
- Incident notification SLA

---

## Data Processing Addendum (DPA / UPP)

Mandatory under GDPR Art. 28 whenever vendor processes personal data on buyer's behalf.

### Required by Art. 28(3) — see eu-poland-checklist.md §2b

Every item in that checklist must be present. Missing items in a DPA are more serious than in a T&C because the law literally requires them.

### Things to look for additionally

- **Defined "data importer / exporter" roles** (if international transfer involved)
- **Annex / Schedule with TOMs** (Technical and Organisational Measures) — vague TOMs are 🟠 NEGOTIATE
- **Annex with categories of data subjects, data types, processing purposes** — this is the Art. 28(3) "subject matter, nature, purpose" requirement; should be specific, not "as agreed between the parties from time to time"
- **Sub-processor schedule** — list, with notification commitments for changes
- **Audit rights** — at minimum: access to audit reports (SOC 2, ISO 27001), right to ask questions. Strong DPA: on-site audit right with X days notice. Weak DPA: nothing. Some vendors charge for audits — 🟠 NEGOTIATE.
- **International transfer mechanism** — see EU/Poland checklist §2c
- **Liability under DPA** — sometimes a separate cap; sometimes pulls in main agreement's cap. Flag any DPA-specific cap lower than the main contract's.

### EU-specific watch-points

- **EDPB Guidelines on Art. 28** were updated in 2024 — vendor's DPA should be aligned (not citing 2018 guidance).
- **EU AI Act** — if data is being processed by a high-risk AI system (Annex III of AI Act), additional documentation obligations apply. Flag 🟠 if the service is AI-based and the contract doesn't acknowledge AI Act compliance.

---

## NDA / Confidentiality Agreement

### Standard checklist

- [ ] Definition of Confidential Information — specific enough; ideally includes oral disclosures if marked confidential within X days
- [ ] Standard exclusions: already known, publicly available, independently developed, received from third party without obligation
- [ ] Permitted disclosure: by law, court order (with notice to discloser where possible)
- [ ] Use limitation — info usable only for the defined Purpose
- [ ] Duration — survival period (usually 2-5 years; perpetual for trade secrets)
- [ ] Return / destruction of materials on request
- [ ] Remedies — injunctive relief available given inadequacy of monetary damages
- [ ] No reverse engineering

### Common issues

- **One-sided NDA** (only one party's info protected) — fine if only one party is sharing; 🟠 if both parties will exchange info.
- **Perpetual NDA** — unusual; 🟠 NEGOTIATE down to a reasonable term unless the info is genuinely a trade secret.
- **Overbroad Confidential Information** — e.g., "all information of any kind." Should require either marking or reasonable understanding. 🟠.
- **No carve-out for residual knowledge** (information retained in memory of employees) — common in some industries; 🟠 NEGOTIATE for residuals clause if buyer's people regularly work with vendor's competitors.
- **Penalty clause** (kara umowna) for breach — under Polish KC Art. 483-484, allowed for non-monetary obligations. 🟠 NEGOTIATE if disproportionate.
- **Non-compete or non-solicitation hidden inside NDA** — 🟠 NEGOTIATE — these belong in a separate agreement and have specific Polish-law requirements (compensation for non-compete under Art. 1011-1014 KP for employees).

---

## Employment Contract (Umowa o pracę)

Polish Labour Code (Kodeks pracy) governs. Most provisions are mandatory and cannot be derogated from to employee's detriment.

### Required elements (Art. 29 KP)

- [ ] Parties' identities
- [ ] Type of contract (probationary / fixed-term / indefinite)
- [ ] Date of conclusion and start date
- [ ] Place of work
- [ ] Type of work
- [ ] Compensation with specified components
- [ ] Working hours
- [ ] Vacation entitlement and notice period (usually by statutory reference)

### Red flags

- **Probation period > 3 months** → invalid (max 3 months per Art. 25 KP).
- **Non-compete clause without compensation** → invalid (Art. 1011 KP requires compensation of at least 25% of pre-termination salary).
- **Penalty clauses against employee for ordinary breach** → generally invalid (employee liability capped by KP for negligent breach).
- **Waiver of statutory rights (vacation, overtime, etc.)** → invalid.
- **B2B contract with all hallmarks of employment** (subordination, fixed hours, employer's premises) → risk of reclassification by ZUS / labour inspector. ⓘ Major risk if buyer is the contractor.
- **IP assignment clause** — see ip-and-licensing.md. Note: Polish law has automatic transfer rules for employee-created works (Art. 12-14 of Copyright Act — employer acquires rights to works created within employment duties), but only for the specific scope. Outside-duties works need explicit assignment.

### Recently relevant changes (Polish labour law)

- **2023 transposition of Work-Life Balance and Transparent Working Conditions directives** — more information rights, paternity/parental leave updates, carer's leave. Flag if contract template looks pre-2023.
- **Remote work (praca zdalna)** — codified in KP as of April 2023. Should have telework rules if any remote work is involved.
- **Whistleblower Protection (Ustawa o ochronie sygnalistów)** — in force since Sept 2024. Companies > 50 employees must have internal reporting procedure. Flag if contract is for such a company and references confidentiality in a way that conflicts with whistleblower rights — confidentiality cannot block legally protected reporting.

---

## Vendor / Supplier / Purchase Agreement

For goods purchase or services other than SaaS.

### Standard checklist

- [ ] Specification / scope of goods or services (with annex if detailed)
- [ ] Delivery / performance terms (date, place, INCOTERMS if international goods)
- [ ] Price and payment terms (typical: net 30 / 60 in PL; 30-day max for B2B under Art. 5 of Anti-Late-Payments Act)
- [ ] Acceptance procedure (especially for IT services / dev work)
- [ ] Warranty (rękojmia) — under PL KC, applies by law for 2 years on goods sold to consumers, 1 year minimum for B2B; can be extended/limited contractually for B2B
- [ ] Guarantee (gwarancja) — optional, separate from rękojmia
- [ ] Liquidated damages (kara umowna) for delay, defects, breach
- [ ] Termination

### Red flags

- **Payment term > 60 days** for B2B → potentially abusive under PL Anti-Late-Payments Act unless objectively justified. 🟠 NEGOTIATE.
- **Statutory late-payment interest disclaimed** → flag; statutory rate (Art. 359 KC) applies absent agreement, and B2B late payment interest under the Anti-Late-Payments Act is mandatory.
- **One-sided liquidated damages** (kara umowna) — typically vendor pays for delay / defective performance; if only buyer pays anything, 🟠 NEGOTIATE.
- **Rękojmia excluded entirely for B2B** — legally allowed but rare. 🟠 NEGOTIATE.
- **Acceptance "deemed" after silence** — common in IT vendor contracts. 🟠 if too short (e.g., 5 days), 🟢 if reasonable (15-30 days).
- **No IP assignment for dev work** — for IT services where vendor delivers custom software, buyer should own resulting code. See IP reference. 🟠 NEGOTIATE.

### Retail-specific (relevant given buyer's sector)

- **Supplier abuse practices law** (Ustawa o przeciwdziałaniu nieuczciwemu wykorzystywaniu przewagi kontraktowej) — applies to agri-food retail; if buyer is in agri-food retail, specific list of forbidden practices.
- **Returns / chargebacks for retail goods** — typical for B2B retail-supplier relationships; check that terms are reasonable and well-defined.
- **Minimum-order quantities / take-or-pay** — flag if buyer is locked into volume commitments.

---

## License Agreement / Software License

See ip-and-licensing.md (esp. §2) for full OSS license analysis.

### Standard checklist

- [ ] Grant of license — scope (use, modify, distribute, sublicense)
- [ ] Territory
- [ ] Duration (perpetual vs. term)
- [ ] Exclusivity (exclusive, non-exclusive, sole)
- [ ] Permitted users (e.g., "Buyer's employees and contractors" or "5 named users" or "enterprise-wide")
- [ ] Restrictions (no reverse engineering, no benchmarking, no removal of notices)
- [ ] Fields of use (e.g., "internal business operations only")
- [ ] Maintenance and support — separately licensed or included
- [ ] Audit rights (vendor auditing buyer's license compliance — common in enterprise software)
- [ ] Source-code escrow (for mission-critical software)

### Red flags

- **Vendor's audit right with broad scope and short notice** — common in MS, Oracle, IBM contracts. 🟠 NEGOTIATE — limit frequency (1/year), require business-hours, NDA-protected, no fishing expeditions.
- **"License compliance" penalties** — payment of back-license fees + treble damages + audit costs. 🔴 if no cap; 🟠 if reasonable.
- **Per-user / per-CPU / per-named-user metric ambiguity** — define every counting unit precisely.
- **Software-as-a-Service hidden behind a "license"** — when vendor controls the software (cloud-only), most "license terms" don't apply; structure should be a service agreement. 🟠 NEGOTIATE for proper structure.
- **No transfer right** — buyer can't sublicense to subsidiaries, can't transfer in corporate transactions. 🟠 NEGOTIATE for "affiliate use" and "corporate-transaction" transfer.

---

## Quick reference: which checklists apply

| Contract description suggests... | Checklists to use |
|---|---|
| "Anthropic Commercial Terms," "AWS Customer Agreement," etc. | T&C/SaaS + DPA (if data) + IP (if AI/dev) + EU/Poland |
| "Data Processing Addendum" | DPA + EU/Poland (focus on §2) |
| "Mutual NDA" | NDA + EU/Poland (focus on §1, §9) |
| "Master Services Agreement" | T&C/SaaS + Vendor + DPA + IP + EU/Poland |
| Vendor delivering custom software | Vendor + IP (with focus on assignment) + EU/Poland |
| Vendor supplying goods | Vendor + EU/Poland |
| "Open-source review" / GitHub repo LICENSE file | IP/licensing only |
