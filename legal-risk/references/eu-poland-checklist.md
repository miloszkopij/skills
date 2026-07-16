# EU / Poland Legal Checklist

Apply this checklist to **every** contract. The user is a Poland-based, EU-area buyer. The legal frame is GDPR + Polish Civil Code (Kodeks cywilny) + relevant EU directives.

---

## 1. Governing Law and Jurisdiction

**Default position:** Polish law, Polish courts (or at minimum, an EU member-state law and an EU court).

| Found in contract | Severity | Reason |
|---|---|---|
| Polish law, Polish court | 🟢 ACCEPTABLE | Ideal |
| Irish/Dutch/German/other EU law, EU court | 🟢 ACCEPTABLE | Standard for US SaaS via EU entity |
| English law (post-Brexit), UK court | 🟠 NEGOTIATE | No longer EU; enforcement harder |
| US state law (California, Delaware, NY), US court | 🔴 DEAL_BREAKER → at minimum 🟠 NEGOTIATE | Forces buyer into foreign forum; expensive to litigate; B2C protections lost |
| Arbitration in non-EU venue (Singapore, HK, US) | 🟠 NEGOTIATE | Workable but pricy; check arbitration body (JAMS, ICC, AAA) |
| Arbitration in Dublin / Stockholm / Geneva | 🟢 ACCEPTABLE | Common, neutral |
| "Mandatory jury waiver" / "class action waiver" | ⓘ INFORMATIONAL for B2B | Standard in US contracts; binding on EU parties is questionable but typically signable |

**Polish-specific:** Under Art. 1104 KPC, parties can freely choose foreign jurisdiction for commercial matters. So foreign jurisdiction is *legally* fine for B2B, just *practically* bad.

---

## 2. GDPR / RODO Compliance

Required whenever the contract involves processing personal data (which is almost always, even if just employee emails).

### 2a. Is there a DPA?

If the contract involves the vendor processing any personal data on behalf of the buyer, a Data Processing Addendum (Umowa Powierzenia Przetwarzania Danych) is **mandatory under GDPR Art. 28**. Missing DPA = 🔴 DEAL_BREAKER.

### 2b. Required elements of Art. 28(3) DPA — checklist

The DPA must specify:
- [ ] Subject matter and duration of processing
- [ ] Nature and purpose of processing
- [ ] Type of personal data
- [ ] Categories of data subjects
- [ ] Obligations and rights of the controller (the buyer)
- [ ] Processor acts only on documented instructions
- [ ] Confidentiality obligations on processor's staff
- [ ] Security measures (Art. 32) — TOMs (Techniczne i Organizacyjne Środki)
- [ ] Sub-processor authorization rules (general or specific written authorisation)
- [ ] Assistance with data-subject rights (access, rectification, erasure, etc.)
- [ ] Assistance with security, breach notification, DPIA, prior consultation
- [ ] Deletion or return of data at end of services
- [ ] Audit rights for the controller (at least info + cooperation with audits)

Any missing item = 🟠 NEGOTIATE (or 🔴 if multiple missing).

### 2c. International transfers (Schrems II)

If data goes outside EEA (typically: US-based vendor):

| Transfer mechanism | Status |
|---|---|
| Adequacy decision (e.g., UK, Switzerland, Japan, S. Korea, Canada for commercial orgs) | 🟢 ACCEPTABLE |
| EU-US Data Privacy Framework (DPF) certified | 🟢 ACCEPTABLE (but unstable — Schrems III pending; flag as ⓘ) |
| Standard Contractual Clauses (SCCs 2021/914) | 🟢 ACCEPTABLE if correct module |
| SCCs + Transfer Impact Assessment (TIA) | 🟢 ACCEPTABLE — best practice |
| Only "we comply with applicable laws" with no SCCs/adequacy | 🔴 DEAL_BREAKER |
| Old 2010 SCCs | 🔴 DEAL_BREAKER (invalid since Dec 2022) |

**SCC modules:**
- Module 1: Controller → Controller
- Module 2: Controller → Processor (most common for SaaS)
- Module 3: Processor → Processor (sub-processor chains)
- Module 4: Processor → Controller (rare)

Flag wrong module as 🟠 NEGOTIATE.

### 2d. Sub-processors

- Vendor should list current sub-processors (or link to a maintained page).
- General written authorisation + notice of changes with right to object → 🟢 ACCEPTABLE.
- Specific authorisation required for each → 🟢 ACCEPTABLE (more buyer-friendly).
- Vendor can change sub-processors at will with no notice → 🔴 DEAL_BREAKER (violates Art. 28(2)).

### 2e. Breach notification timing

- ≤ 24h or ≤ 48h → 🟢 ACCEPTABLE
- ≤ 72h (matches buyer's GDPR Art. 33 obligation) → 🟢 borderline; ideally faster
- "Without undue delay" with no number → 🟠 NEGOTIATE (push for ≤48h)
- "Reasonable time" / no commitment → 🔴 DEAL_BREAKER

### 2f. Buyer's specific Polish concerns

- **UODO** (Urząd Ochrony Danych Osobowych) is the Polish supervisory authority; contract should not prevent cooperation with it.
- Polish Labour Code adds extra protection for employee data — flag if employees' data is in scope.

---

## 3. Liability

### 3a. Liability cap

Typical SaaS: capped at 12 months of fees paid. This is standard.

| Cap | Severity |
|---|---|
| 12 months fees, mutual cap | 🟢 ACCEPTABLE |
| 12 months fees, only on vendor's side; buyer has unlimited liability | 🔴 DEAL_BREAKER |
| 6 months or less | 🟠 NEGOTIATE |
| Fixed amount (e.g., €10,000) vs. fees-based, when fees are low | 🟠 depends; check if proportionate to risk |
| Total exclusion of liability | 🔴 DEAL_BREAKER (also unenforceable under Polish law per Art. 473 KC for willful misconduct) |

### 3b. Carve-outs from the cap

Standard carve-outs (cap does NOT apply to):
- Indemnification obligations
- Confidentiality breach
- IP infringement
- Gross negligence / willful misconduct (in Poland, this is mandatory under Art. 473 KC — can't be excluded)
- Data breach (often, sometimes super-cap of 2x fees)

| Found | Severity |
|---|---|
| Standard list of carve-outs above | 🟢 ACCEPTABLE |
| No carve-outs at all | 🟠 NEGOTIATE |
| Vendor's data-breach liability inside the cap | 🟠 NEGOTIATE — push for super-cap or carve-out |

### 3c. Polish law mandatory limits

Under Polish Civil Code:
- **Art. 473 §2 KC** — liability for willful misconduct (wina umyślna) cannot be excluded in advance. Any clause attempting this is void.
- **Art. 449 KC** — product liability cannot be excluded toward consumers (B2C only).

Flag any blanket "exclusion of all liability" as 🔴 (it's partially unenforceable and shows the contract wasn't reviewed for PL law).

---

## 4. Termination

| Found | Severity |
|---|---|
| Either party may terminate for convenience with 30+ days notice | 🟢 ACCEPTABLE |
| Only vendor may terminate for convenience; buyer is locked in | 🔴 DEAL_BREAKER |
| Only buyer locked into multi-year auto-renewal with short opt-out window | 🟠 NEGOTIATE |
| Termination for material breach with cure period (30 days) | 🟢 ACCEPTABLE |
| Immediate termination by vendor for vague "violation of policies" | 🟠 NEGOTIATE — define what triggers it |
| Suspension rights — vendor can suspend service "at sole discretion" | 🟠 NEGOTIATE |
| No data return / export upon termination | 🔴 DEAL_BREAKER for SaaS handling buyer's data |
| Auto-renewal with no notice requirement | 🟠 NEGOTIATE (note Polish consumer rules don't apply to B2B but transparency is good practice) |

---

## 5. Indemnification

### 5a. IP indemnity (vendor protects buyer)

Required for SaaS / software. Vendor should defend & indemnify buyer against third-party IP claims arising from buyer's authorised use.

| Found | Severity |
|---|---|
| Full IP indemnity, including reasonable attorneys' fees | 🟢 ACCEPTABLE |
| IP indemnity with standard exclusions (modifications, combinations, etc.) | 🟢 ACCEPTABLE |
| No IP indemnity at all | 🟠 NEGOTIATE (sometimes 🔴 depending on what the product is) |
| IP indemnity excludes AI-generated outputs / open-source components | 🟠 NEGOTIATE — significant exposure for IT buyers |

### 5b. Buyer's indemnity to vendor

Buyer typically indemnifies for:
- Buyer's data / inputs infringing third-party rights
- Buyer's use violating acceptable use policy
- Buyer's misuse of outputs

These are standard. 🟢 ACCEPTABLE if balanced.

Flag as 🔴 if buyer's indemnity is open-ended ("any claims relating to Customer") or if there's no corresponding vendor indemnity.

---

## 6. Fees and Payment

| Found | Severity |
|---|---|
| Vendor may unilaterally raise prices with X days notice | 🟠 NEGOTIATE if X < 60; cap annual increases (e.g., max CPI or 5%) |
| Late payment interest at statutory rate | 🟢 ACCEPTABLE |
| Late payment interest > statutory + 10pp | 🟠 NEGOTIATE |
| Gross-up clauses for withholding tax | ⓘ INFORMATIONAL — check with PL tax advisor if PL-source payments to non-PL vendor |
| Service suspension for late payment without cure | 🟠 NEGOTIATE — push for 15-day cure |

**Polish VAT:** Cross-border B2B services typically reverse-charge VAT (buyer accounts for it). Flag any clause that requires buyer to pay vendor's local VAT.

---

## 7. Cross-border considerations specific to Poland

- **NBP exchange rate clauses** — if contract is in foreign currency, check whether exchange rate is fixed or floating, and reference (NBP average vs. ECB, etc.).
- **Polish-language requirement** — for contracts with Polish consumers, Polish-language version is required (Ustawa o języku polskim). For B2B, not required, but bilingual contract is best practice if Polish-side employees need to operate under it.
- **Notarial / written form requirements** — most B2B contracts are valid in written form (including electronic). Real estate, share transfers, and certain IP assignments need notarial form (akt notarialny). Flag if the contract claims to do something requiring notarial form but isn't notarised.
- **Electronic signature** — qualified electronic signature (kwalifikowany podpis elektroniczny) is equivalent to handwritten in Poland under eIDAS. DocuSign etc. are advanced electronic signatures, valid but slightly weaker evidentiary value.

---

## 8. Force Majeure

Mostly boilerplate. Flag only if:
- Force majeure excuses payment obligations (🟠 — unusual; buyer still has to pay even if vendor can't deliver?)
- Force majeure includes "any government action" without limit (🟠)
- No force majeure clause at all (ⓘ — defaults to KC Art. 471 doctrine of impossibility; usually fine)

---

## 9. Confidentiality

Standard items:
- Definition of Confidential Information
- Exclusions (public knowledge, independently developed, etc.)
- Survival period after termination (typically 2-5 years; perpetual for trade secrets)
- Required disclosure (court order) carve-out

🟠 NEGOTIATE if:
- No survival period stated
- Definition is one-sided (only vendor's info protected, not buyer's)
- Perpetual confidentiality for ALL info (impractical)

🔴 if:
- No confidentiality clause at all in a contract involving buyer's business data

---

## 10. Publicity / Marketing

Vendor wants to list buyer as a customer. Default: opt-out should exist.

| Found | Severity |
|---|---|
| Opt-out mechanism provided | 🟢 ACCEPTABLE |
| Opt-in required (vendor needs buyer's permission) | 🟢 ACCEPTABLE (best for buyer) |
| Vendor may use buyer's name/logo with no opt-out | 🟠 NEGOTIATE |
| Vendor may publish quotes / case studies without approval | 🟠 NEGOTIATE |

For retail-sector buyers: brand control matters more than for IT — push harder on opt-in.
