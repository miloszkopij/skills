---
name: it-vendor-review
description: >
  Deep IT sector specialist for reviewing and risk-assessing vendor contracts for software, SaaS, hardware, licensing, cloud, and IT services agreements. Use this skill ALWAYS when the user uploads or pastes a vendor contract and asks to review it, check it, assess risk, or says anything like "is this OK to sign?", "what's wrong with this contract?", "check the SLA", "review this vendor agreement", "assess this deal" — even without the word "IT". This skill goes deep on operational risk that legal-risk skill doesn't: SLA benchmarks (uptime thresholds, response/resolution tiers, credit formulas), software license traps (seat counts, audit rights, true-up mechanics), hardware maintenance and EOL risk, pricing escalation clauses, cloud egress/lock-in, data sovereignty, and vendor exit strategy. Specialized for a Poland/EU buyer. Produces a structured markdown risk report (plus an annotated .docx on request) with severity-tagged findings and negotiation guidance. Prefer this skill over legal-risk for any IT/tech vendor contract.
---

# IT Vendor Contract Review

A deep-specialist skill for assessing vendor contracts in the IT sector — software, SaaS, cloud, hardware, licensing, and managed services — from the perspective of a **Poland/EU-based buyer**.

The skill surfaces **operational and commercial** red flags that a pure legal review often misses: weak SLA math, dangerous pricing mechanics, licensing audit traps, lock-in structures, EOL risk, and exit barriers.

---

## When to use this skill

Trigger on any vendor paper involving:
- **SaaS / cloud services** (CRM, ERP, collaboration, security, AI/LLM APIs)
- **Software licenses** (perpetual, subscription, enterprise, OEM, open-source commercial)
- **Hardware supply or maintenance** (servers, network equipment, endpoints, peripherals)
- **Managed IT services** (MSP, NOC/SOC, helpdesk, infrastructure management)
- **Custom software development** (bespoke apps, staff augmentation with IP components)
- **Cloud infrastructure** (IaaS/PaaS — AWS, Azure, GCP reseller or direct agreements)
- **Telecom / connectivity** (leased lines, SD-WAN, VoIP)

---

## Output format

Deliver findings in two tiers:

### In-chat summary (always)
- Overall verdict: ✅ SIGN / ⚠️ NEGOTIATE / 🚫 WALK AWAY
- Severity counts: 🔴 Critical / 🟠 High / 🟡 Medium / ⓘ Informational
- Top 3–5 critical findings, one line each
- Compliance checklist (SLA ✅/❌, GDPR ✅/❌, Licensing ✅/❌, Liability ✅/❌, Exit ✅/❌, IP ✅/❌)

### Full report (always — markdown file)
Save `<original_name>_it_review.md`: executive summary first, then all findings in document order. Comments in **Polish**, replacement wording in the **contract's language**. Per-finding format:

```markdown
### [🔴 KRYTYCZNE | KATEGORIA: SLA] Sekcja X.Y — <short title>
> "verbatim anchor quote from the clause (≤15 words)"

<Polish explanation of the problem and why it matters for this buyer>

**Sugerowana zmiana:**
> <replacement wording in contract language>
```

### Annotated .docx (on user request)
The full original contract with real Word comments anchored to clauses and the executive summary prepended as page 1 — produced with the bundled `scripts/docx_tool.py` (Python 3 stdlib only, works in any environment). Offer this when the user wants a file for Word or for the vendor.

---

## Workflow — follow in order

### Step -1 — Input handling (do this first, before anything else)

The contract may arrive in any form. Work in the current working directory (or the environment's designated output folder). Handle each as follows:

**Provided .docx file**
- Extract the full text: `python3 scripts/docx_tool.py extract <file.docx>`. Keep the original untouched — it is the annotation base if the user requests a .docx deliverable.

**Provided .pdf file**
- Extract text with whatever is available, in this order: an environment PDF-reading capability; `pdftotext` (poppler); `pypdf`/`pdfplumber` if installed or installable. If none works, ask the user to paste the text.

**URL / hyperlink**
- Fetch with the environment's web-fetch capability (or `curl -L` where network access is allowed); extract all clause text, preserving section numbers.
- If the URL requires login or returns no content: inform the user and ask them to paste the text or upload the file directly.
- Always record the URL and fetch date in the executive summary's verification section.

**Pasted plain text**
- Use it directly, preserving all section numbering and headings.

**No document provided yet**
- Ask: "Proszę o przesłanie umowy — można wgrać plik (.docx lub .pdf), wkleić tekst lub podać link do dokumentu."

#### CRITICAL: Full document coverage

**Analyze the ENTIRE original document — every paragraph, clause, annex, schedule, and appendix — and reference findings by exact section numbers with verbatim anchor quotes.** Never work from only "key", "problematic", or "selected" sections. If a .docx deliverable is requested, it must contain every paragraph of the original — comments annotate the original, they don't replace it.

**The full report is always a saved file, never chat text only.** Always write the markdown report to disk; produce the annotated `.docx` additionally when the user requests it.

### Step 0 — Establish context (always; one question round — use a structured question tool if the environment has one, otherwise plain chat)

Before analysis, capture what isn't already clear from the contract or conversation:

1. **Contract type** — SaaS / perpetual license / hardware / MSP / custom dev / cloud infra / other
2. **Criticality** — PoC / production non-critical / production-critical / business-critical (revenue/operations stops if this vendor fails)
3. **Data processed** — none / internal non-sensitive / customer personal data (GDPR scope) / regulated (financial, health, biometric)
4. **Vendor geography** — EU/EEA vendor / US vendor / other non-EEA

Use answers to re-grade severity (see `references/severity-grading.md`).

### Step 1 — Load the relevant reference checklist

Read **all** applicable reference files from `references/`:

| Contract type | Reference file |
|---|---|
| SaaS / cloud service | `sla-and-cloud.md` |
| Software license | `software-licensing.md` |
| Hardware / maintenance | `hardware-and-maintenance.md` |
| MSP / managed services | `managed-services.md` |
| Custom software dev | `custom-dev.md` |
| Any contract (always) | `universal-checks.md` |
| GDPR relevant (always if personal data involved) | `gdpr-and-data.md` |

Read `universal-checks.md` for every review. Add others as applicable.

### Step 2 — Analyse

Work through each checklist item. For each:
- Locate the relevant clause (or note its absence)
- Assess: acceptable / negotiate / critical / missing
- Note the specific clause anchor text for placing the Word comment

**Absence is a finding.** If a critical clause is missing entirely, flag it — missing SLA is as dangerous as a bad one.

Apply the severity grading adjustments for the buyer's context (Step 0).

### Step 3 — Build executive summary

Write in Polish. Include:

```
# Podsumowanie — ocena kontraktu IT

**Rekomendacja: PODPISAĆ / NEGOCJOWAĆ / ODRZUCIĆ**
**Kontekst: [contract type], [vendor geography], [criticality], [data type]**

## Liczba ustaleń
- 🔴 Krytyczne: N
- 🟠 Wysokie: N
- 🟡 Średnie: N
- ⓘ Informacyjne: N

## Kluczowe problemy
1. [Tytuł problemu] — sekcja X.Y
   [2–3 zdania: co dokładnie jest nie tak, dlaczego to zagraża kupującemu, jaka jest podstawa prawna lub benchmark rynkowy.]
2. [Tytuł problemu] — sekcja X.Y
   [2–3 zdania: opis problemu, konsekwencje, uzasadnienie.]
3. ...

## Checklist
- SLA / dostępność: ✅/❌/⚠️
- GDPR / RODO: ✅/❌/⚠️
- Licencjonowanie: ✅/❌/⚠️
- Ograniczenie odpowiedzialności: ✅/❌/⚠️
- Warunki wyjścia (exit): ✅/❌/⚠️
- Własność intelektualna: ✅/❌/⚠️
- Transfer danych poza EOG: ✅/❌/⚠️ (jeśli dotyczy)

## Uwagi operacyjne
[2–4 zdania: biggest operational risk in plain language]
```

### Step 4 — Write the markdown report

Save `<original_name>_it_review.md` in the working/output directory: executive summary (Step 3) first, then all findings in document order per the format in "Output format".

### Step 4b — Annotated .docx (only when the user asks for a Word file)

Use the bundled `scripts/docx_tool.py` (Python 3 stdlib only):

1. **Annotation base:** the original `.docx` if that was the source; otherwise build one from the full contract text (ALL sections preserved): `python3 scripts/docx_tool.py create contract_full.md working.docx`
2. **Write `summary.md`** (Polish executive summary, markdown) and **`findings.json`** — plain text in JSON, escaping handled by the script:
   ```json
   {"author": "IT Vendor Review", "initials": "IT", "summary": "summary.md",
    "findings": [
      {"anchor": "<clause text appearing verbatim in the contract>",
       "comment": "[🔴 KRYTYCZNE | KATEGORIA: SLA]\n<Polish explanation>\n\nSugerowana zmiana:\n\"<replacement wording>\""}
    ]}
   ```
3. **Run:** `python3 scripts/docx_tool.py annotate working.docx findings.json <original_name>_it_review.docx`
4. Unmatched anchors are reported on stderr (exit code 2) — fix and re-run. If Python 3 is unavailable, deliver the markdown report and explain.

### Step 5 — Deliver

Save the deliverable(s), give the user the exact file path(s) (use the environment's file-presentation mechanism if one exists), and give a 3–5 sentence verbal summary in chat.

---

## Critical rules

- **Always buyer perspective.** Which clauses hurt the buyer, which protections are missing for the buyer.
- **Poland/EU home jurisdiction.** Any clause forcing non-EU forum, non-EU governing law, or non-EEA data processing without SCCs is at minimum 🟠 HIGH.
- **SLA math matters.** Don't just note "SLA exists" — calculate: what does the credit formula actually pay out? What's the real exposure? State it in PLN/EUR if contract value is known.
- **Absence = finding.** Flag missing SLA, missing exit clause, missing data return clause, missing IP ownership clause.
- **No invented findings.** Don't pad — a clean clause gets no comment.
- **Polish for comments, contract language for suggested rewording.** Never mix.
- **Don't rely on memory for legal citations.** If citing GDPR article numbers, Polish KC articles, or specific regulatory deadlines, verify current text via web search within this session. If the environment has no web access, mark citations as unverified in the report and recommend re-verification.
- **ALWAYS cover the full original document.** Analyze every paragraph; a .docx deliverable must contain every paragraph of the original — not just clauses with findings. Creating a partial document with only commented paragraphs is a critical failure mode.
- **Never assume platform-specific tools or paths.** Use only relative paths, the bundled `scripts/docx_tool.py`, and capabilities the current environment actually exposes.

---

## Bundled script

- `scripts/docx_tool.py` — stdlib-only Python 3 helper: `extract` text from a .docx, `create` a .docx from markdown-ish text, `annotate` a .docx with Word comments + prepended executive summary. Run `python3 scripts/docx_tool.py` for usage.

## Reference files

Load these based on contract type (always load `universal-checks.md`):

- `references/universal-checks.md` — Clauses to review in every IT contract regardless of type
- `references/sla-and-cloud.md` — SaaS, cloud, uptime SLA benchmarks, credits, cloud lock-in
- `references/software-licensing.md` — License types, audit traps, true-up, open source, IP
- `references/hardware-and-maintenance.md` — Hardware supply, warranty, maintenance SLA, EOL/EOS
- `references/managed-services.md` — MSP/NOC/SOC, service scope, shared responsibility
- `references/custom-dev.md` — Bespoke development, acceptance, IP assignment, escrow
- `references/gdpr-and-data.md` — GDPR Art. 28 DPA, cross-border transfers, data return
- `references/severity-grading.md` — How to re-grade severity based on buyer context
