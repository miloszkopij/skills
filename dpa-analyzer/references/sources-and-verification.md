# Sources and Verification Protocol

The legal landscape changes constantly. The reference files in this skill encode a snapshot of legal knowledge that **must be verified against current sources** before being relied upon in any comment delivered to the user. This file lists authoritative sources and a verification protocol.

---

## Core principle

**No finding may cite a specific legal authority (article number, regulation, case, guideline, deadline) without at least one verification search confirming the cited authority is current.**

If a search reveals the cited authority has been amended, superseded, or reinterpreted, update the comment accordingly. If a search reveals new authority that changes the analysis, incorporate it.

If a search is inconclusive (results unclear, sources outdated, conflicts), say so in the comment ("status pozostaje niepewny — należy skonsultować z zewnętrznym doradcą prawnym") rather than confidently asserting.

---

## Mandatory verification triggers

Always run a verification search when a finding involves any of:

1. **A specific article number** of an EU regulation, EU directive, or Polish statute
2. **A specific deadline or effective date** (EU AI Act phases, CRA timelines, NIS2 transposition, DORA application, etc.)
3. **A reference to a CJEU or Polish court ruling** (e.g., Schrems II, the validity of the EU-US DPF)
4. **An EDPB / EDPS / UODO guideline or decision**
5. **A standard contractual clause module / version** (SCC 2021/914 — was it replaced?)
6. **An open-source license interpretation** (FSF/OSI positions can shift; some licenses get court tests)
7. **The status of an adequacy decision** (e.g., UK adequacy renewed? Japan still adequate? Korea still adequate for commercial orgs?)
8. **Any regulatory regime where the contract is being signed for compliance** (financial → DORA, critical infrastructure → NIS2, products with digital elements → CRA, AI → AI Act)

For findings that don't touch the above (e.g., "this liability cap is below market," "this NDA has no survival period"), no verification search is required — they're judgment calls, not legal-citation calls.

---

## Authoritative sources, ranked

When verifying, prefer in this order:

### Tier 1 — Primary law and regulators

| Source | What it has | URL |
|---|---|---|
| **EUR-Lex** | Consolidated text of all EU legislation; tells you if a regulation is in force, amended, repealed | `eur-lex.europa.eu` |
| **CURIA** | CJEU judgments — controlling for EU-law interpretation | `curia.europa.eu` |
| **ISAP (Sejm)** | Polish statutes in current form (the Polish equivalent of EUR-Lex's "consolidated text") | `isap.sejm.gov.pl` |
| **EDPB** | Guidelines, recommendations, binding decisions on GDPR | `edpb.europa.eu` |
| **EDPS** | EU institutions' DPA; sometimes leads policy direction | `edps.europa.eu` |
| **UODO** | Polish data protection authority — decisions, guidance | `uodo.gov.pl` |
| **European Commission** | Adequacy decisions, infringement procedures, implementation status | `commission.europa.eu` |
| **EU AI Office** | AI Act implementation guidance | `digital-strategy.ec.europa.eu/en/policies/ai-office` |
| **ENISA** | NIS2 / cybersecurity guidance | `enisa.europa.eu` |

### Tier 2 — Polish courts and supplementary

| Source | What it has | URL |
|---|---|---|
| **SN (Sąd Najwyższy)** | Polish Supreme Court rulings | `sn.pl` |
| **NSA (Naczelny Sąd Administracyjny)** | Polish administrative court rulings (relevant for UODO appeals) | `nsa.gov.pl` |
| **Trybunał Konstytucyjny** | Constitutional rulings | `trybunal.gov.pl` |
| **Rządowe Centrum Legislacji** | Polish legislation in process | `rcl.gov.pl` |

### Tier 3 — Practitioner sources (use with caution)

Useful for "is this interpretation current" sanity checks, never as sole authority:
- Major law firm publications (Dentons, Bird & Bird, DLA Piper, CMS, local: WKB, SK&S, KKLW)
- IAPP (`iapp.org`) for GDPR practice
- Software Freedom Conservancy / SFLC for open-source license questions
- OSI (Open Source Initiative — `opensource.org`) for license categorisation

### Tier 4 — Avoid as authority

- Wikipedia (use for orientation only, never cite)
- AI-generated legal summaries (including from other AIs)
- Out-of-date blog posts (always check the date — anything older than 18 months on a fast-moving topic is suspect)
- Marketing pages of legal-tech vendors

---

## Verification search patterns

### Quick checks

| What you're checking | Good query |
|---|---|
| Is GDPR Art. 28 still as I remember? | `"GDPR Article 28" consolidated text` → eur-lex.europa.eu |
| Has SCC 2021/914 been replaced? | `Standard Contractual Clauses 2021 914 status` |
| Is UK still adequate? | `UK adequacy decision GDPR status` |
| EU-US DPF still valid? | `EU US Data Privacy Framework status` |
| When does CRA apply? | `Cyber Resilience Act application date` |
| EU AI Act current phase? | `EU AI Act 2026 obligations in force` |
| Has UODO ruled on X? | `UODO decyzja <topic>` |
| Is BUSL / SSPL OSI-approved? | `<license name> OSI approved` |

### Deeper checks

For findings that go into a deal-breaker comment, do at least two searches:
1. One to confirm the cited authority's current status
2. One to look for recent enforcement / interpretation (last 18-24 months)

For an EU buyer-perspective contract review, particularly worth checking each time:

- **Schrems III status** — there's ongoing litigation about EU-US DPF; status can shift quickly
- **Polish Whistleblower law (Ustawa o ochronie sygnalistów)** — relatively new (Sept 2024), implementation guidance evolving
- **DORA scope** — applies from 17 Jan 2025 for in-scope financial entities; vendor contracts referencing DORA should be checked
- **NIS2 transposition in Poland** — Poland was late on transposition; check status
- **AI Act prohibited practices** in force since 2 Feb 2025; GPAI obligations from 2 Aug 2025; high-risk system obligations from 2 Aug 2026; check what's currently applicable
- **CRA timeline** — adopted 2024; main obligations apply from late 2027, but reporting obligations earlier

(Some of these dates may have shifted — verify rather than relying on the list above.)

---

## When sources conflict

If primary law (Tier 1) and a practitioner source (Tier 3) disagree, primary law wins, but flag the conflict in the comment ("interpretacja praktyki rynkowej różni się od literalnego brzmienia przepisu — w razie sporu interpretacja organu nadzorczego jest decydująca").

If two Tier 1 sources appear to conflict, the more recent and more specific wins (lex posterior, lex specialis), but say so explicitly in the comment.

If no source directly addresses the issue, say so. Never invent authority.

---

## What to do with vendor-specific facts

If the contract names specific things — vendor entity, sub-processors, certifications, schedules — and the user wants thorough review, consider a search for:

- **Vendor's published sub-processor list** — does it match what the DPA references?
- **Vendor's published security certifications (SOC 2, ISO 27001)** — is the date current?
- **Vendor's recent enforcement actions / public incidents** — informational only, but worth surfacing if material
- **Vendor's published DPA / updates** — sometimes the DPA the user has is an outdated version

Don't go on a vendor-research expedition by default — only when the contract analysis specifically benefits from external facts.

---

## Logging searches in the output

In the executive summary, include a small **"Weryfikacja źródeł"** subsection listing the key authorities consulted and the date of consultation:

```
## Weryfikacja źródeł
Niniejsza analiza opiera się na następujących źródłach (zweryfikowanych dn. <data>):
- RODO (Rozporządzenie 2016/679) — tekst skonsolidowany EUR-Lex
- Standardowe Klauzule Umowne (Decyzja KE 2021/914) — status: obowiązują
- Wytyczne EDPB nr [X] z [data]
- [inne specyficzne źródła użyte w analizie]
```

This makes the analysis auditable and lets the user verify any specific point.

---

## Hard rule

If asked about something the skill genuinely doesn't know and can't verify (e.g., niche industry regulation, jurisdiction-specific tax matter, very recent legislative change still in transposition), the comment should say so directly:

> "Klauzula dotyczy [obszaru]. Aktualne brzmienie przepisów krajowych w tym zakresie wykracza poza zakres niniejszej analizy. Rekomendujemy konsultację z doradcą podatkowym / prawnym specjalizującym się w [obszarze] przed podpisaniem."

Better to admit a gap than to confidently mislead.
