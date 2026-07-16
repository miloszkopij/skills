---
name: legal-risk
description: "Substitute legal advisor for analyzing and commenting on contracts, terms of service, DPAs, NDAs, SaaS agreements, employment contracts, vendor and licensing agreements. Use ALWAYS when the user invokes 'legal-risk', 'legal-risk-skill', 'legal risk skill', or asks for legal review, contract risk assessment, T&C analysis, or DPA review — including when they paste a URL or text of legal terms. Captures the buyer's actual use case (use type, data exposure, output destination, criticality) before analysis and re-grades severity contextually. Verifies cited legal authorities against current sources (EUR-Lex, CURIA, ISAP, EDPB, UODO) when web access is available. Produces a Polish-commented markdown risk report — and, on request, an annotated .docx with Word comments — with severity-tagged findings (deal-breaker / negotiate / acceptable / informational), suggested rewording in the contract's language, and an executive summary. Specialized for Poland/EU IT and retail buyers; covers GDPR, Polish Civil Code, IP law, open-source licenses, and Schrems II."
---

# Legal Risk

A substitute-for-legal-advisor skill for analyzing contracts and producing a commented risk report for negotiation. Specialized for a **Poland/EU-based IT and retail company** that is **always the buyer** signing someone else's paper.

This skill is environment-agnostic: it works in Claude Code, Codex, OpenCode, or any agent runtime with a shell and Python 3. It never depends on platform-specific tools or paths. The bundled `scripts/docx_tool.py` is stdlib-only.

## When to use this skill

Use whenever the user wants legal review of any contract-like document:
- Terms of Service / Terms and Conditions
- Data Processing Addendums (DPAs)
- NDAs
- SaaS / cloud / software-license agreements
- Employment contracts
- Vendor / supplier agreements
- Open-source license review
- Any "is this safe to sign?" question

Triggers include the exact phrase **"legal-risk"** (or **"legal-risk-skill"** / **"legal risk skill"** for backward compatibility), but also less explicit asks like "review these terms," "is this DPA OK?", "what's risky in this contract?"

## Output format at a glance

**Primary deliverable — a markdown risk report** saved as `<original_name>_legal_review.md`, containing:

1. **Executive summary** (first section, in Polish):
   - Severity counts (🔴 deal-breaker, 🟠 negotiate, 🟢 acceptable, ⓘ informational)
   - Top 3–5 deal-breakers, one line each
   - Overall recommendation: **sign / negotiate / walk away**
   - Compliance checklist: GDPR ✅/❌, IP ✅/❌, Jurisdiction ✅/❌, Liability ✅/❌, Termination ✅/❌
2. **Findings in document order**, one subsection per finding:

   ```markdown
   ### [🔴 DEAL-BREAKER | GDPR] Sekcja X.Y — <short title>
   > "verbatim quote of the clause anchor (≤15 words)"

   <Polish comment: what's wrong, why it matters, legal basis>

   **Sugerowana zmiana (do wklejenia):**
   > <replacement wording in the contract's original language>
   ```

3. **Suggested replacement wording** always in the **contract's original language** (so it can be pasted into a counter-proposal); comments always in Polish.

**Secondary deliverable — annotated `.docx` (on user request):** the full original document with real Word comments anchored to clauses and the executive summary prepended as page 1. Produced with the bundled `scripts/docx_tool.py` (Python 3 stdlib only — no installs). Offer this when the user wants a file to open in Word or send to the vendor. No inline tracked changes — only Word comments.

---

## Workflow

Follow these steps in order. Do not skip steps.

### Step 0 — Verify legal currency (always)

Before analyzing, load `references/sources-and-verification.md` and internalize the verification protocol. The reference files in this skill encode a knowledge snapshot that **must be verified against current sources** before being relied upon.

At a minimum, before producing the final analysis, run verification searches for:
- The status of the EU-US Data Privacy Framework (if any US transfer is involved)
- The current SCC version in force (if SCCs are referenced)
- Any specific article of a Polish statute (KC, KP, Copyright Act, etc.) you intend to cite — confirm it has not been amended
- Any specific EU regulation or directive (GDPR, AI Act, DORA, NIS2, CRA, eIDAS, etc.) effective date relevant to the analysis
- Adequacy decision status if a non-EEA jurisdiction other than US/UK/Switzerland is involved

When you cite a specific authority in a comment, you must have verified it within this session. If verification was inconclusive, soften the language in the comment ("zgodnie z aktualnym brzmieniem [X], o ile nie uległo zmianie...") and flag in the executive summary's verification subsection.

**If the environment has no web access** (some Codex/OpenCode configurations), do not skip the analysis. Proceed, but: (a) mark every legal citation as unverified in the executive summary's verification subsection ("źródła niezweryfikowane w tej sesji — stan wiedzy na [snapshot date]"), (b) soften citation language throughout, and (c) recommend the user re-verify DPF status and SCC currency before acting on transfer-related findings.

### Step 0.5 — Capture use-case context (always; only ask what isn't already known)

A contract review without use-case context is a generic checklist. A contract review with use-case context is advice. Two companies signing the same vendor's paper have very different risk profiles depending on what they actually do with the service.

**Before** doing the substantive analysis, capture the four pieces of context below. Ask in a single round, using whatever question mechanism the environment provides (a structured question tool if available, otherwise plain chat). Skip any question whose answer is already evident from earlier conversation or from an obvious reading of the contract (e.g., a Polish-language employment contract uploaded by an HR manager doesn't need "what's the use case" asked).

The four pieces of context:

1. **Primary use case** — what is the buyer actually using this service for? Common categories:
   - Internal employee productivity tool (e.g., drafting, summaries, analysis used inside the company)
   - Customer-facing product feature (chatbot, search, recommendations, generation seen by end customers)
   - Agentic automation (the service takes actions on behalf of the buyer or its users)
   - Fine-tuning / model customization with buyer's data
   - Development, evaluation, R&D (the service itself is the subject of work; outputs aren't deployed)
   - Other / multiple — capture which

2. **Data exposure** — what kind of data goes into Inputs?
   - Public or non-sensitive
   - Internal but non-confidential business data
   - Business confidential / trade secret
   - Customer personal data (GDPR scope)
   - Regulated data (financial, health, biometric, children's data)
   - IP-sensitive content (manuscripts, designs, code, content the buyer paid to license)

3. **Output destination** — where do Outputs go?
   - Internal use only (employees view results, no further distribution)
   - Customer-facing inside the buyer's product (Outputs visible to end users)
   - Published externally (marketing, press, public content, ads)
   - Fed into automated decisions about people (employment, credit, insurance, healthcare, housing, education)
   - Used to train downstream models
   - Used as Customer's product output that buyer sells (e.g., a SaaS where the customer pays for AI-generated reports)

4. **Scale and criticality**
   - Proof of concept / pilot
   - Production but non-critical (some downtime tolerable)
   - Production-critical (revenue-blocking or customer-blocking if unavailable)

**Use the captured context to:**

- **Re-grade severity per finding.** A finding's default severity (from the checklists) is a baseline. The actual severity for THIS buyer depends on use case. Examples:
  - Patent/trademark indemnity carve-out: 🟠 default → 🔴 for retail with Outputs in public marketing; → ⓘ for internal-only use.
  - Beta Services low liability cap: 🟠 default → ⓘ if buyer is in POC; → 🔴 if production-critical.
  - Suspension rights: 🟠 default → ⓘ for non-critical use; → 🔴 for production-critical customer-facing.
  - High-Risk Use Cases / AI Act disclosure obligations: ⓘ default → 🟠 if buyer's use is consumer-facing or in regulated decision domains.
  - Cross-border data transfer / DPA: ⓘ default → 🟠 if customer personal data flows; → 🔴 if regulated data (health, biometrics) flows.
  - Development Partner Mode opt-in: 🟠 default → 🟢 with a brief warning if buyer isn't on the program; → 🔴 if buyer is considering opting in with sensitive data.

- **Skip non-applicable findings entirely.** Don't flag Beta Services if the buyer is on stable APIs only. Don't flag Marketplace clauses if the buyer is direct. Generates focus.

- **Surface use-case-specific absences.** Examples:
  - Production-critical use case but contract has no uptime SLA → 🟠.
  - Customer-facing chatbot but no disclosure clause → AI Act obligation falls entirely on buyer → 🟠.
  - Fine-tuning with personal data but DPA doesn't cover Fine-Tuning Materials specifically → 🟠.

- **Concretize every comment with a use-case-specific consequence.** Where natural, add 1-2 sentences to the Polish comment showing what the finding means for THIS buyer specifically: "Dla Państwa zastosowania (chatbot dla klientów retail) oznacza to, że..." This transforms generic warnings into actionable advice.

- **Reflect the context in the executive summary.** Begin the summary with one sentence stating the assumed context ("Analiza zakłada wykorzystanie usługi do [X] z danymi [Y], Outputs trafiające do [Z], poziom krytyczności [W]"). This makes the analysis auditable: if the assumption was wrong, the reader knows to revisit.

If the buyer indicates multiple use cases, run the analysis from the perspective of the highest-risk one, but note in the executive summary which findings would shift if another use case dominates.

### Step 1 — Intake

Work in the current working directory (or the environment's designated output folder). Determine input type:

- **`.docx` provided** → extract the full text: `python3 scripts/docx_tool.py extract <file.docx>`. Keep the original file untouched — it becomes the annotation base if the user requests a .docx deliverable.
- **`.pdf` provided** → extract text with whatever is available, in this order: an environment PDF-reading capability; `pdftotext` (poppler); `pypdf`/`pdfplumber` if installed or installable. If none works, ask the user to paste the text.
- **URL pasted** → fetch it with the environment's web-fetch capability (or `curl -L` where network access is allowed), extract the legal text, and record the URL and fetch date in the executive summary's verification section. If fetching isn't possible, ask the user to paste the text.
- **Raw text pasted** → use it directly.

#### CRITICAL: Full document coverage

**Analyze and report against the ENTIRE original document — every section, clause, annex, and schedule.** Never work from or reproduce only "key", "problematic", or "selected" paragraphs. In the markdown report, findings must carry exact section numbers and verbatim anchor quotes so the user can locate each clause in their original file. If a .docx deliverable is requested, it must contain every paragraph of the original — comments annotate the original, they don't replace it.

### Step 2 — Classify

Identify the contract type from the text. This decides which checklist file to load next.

| If document is... | Load reference |
|---|---|
| T&C, ToS, EULA, SaaS agreement | `references/contract-type-checklists.md` (T&C section) |
| DPA, data processing addendum | `references/contract-type-checklists.md` (DPA section) + `references/eu-poland-checklist.md` |
| NDA, confidentiality agreement | `references/contract-type-checklists.md` (NDA section) |
| Employment, contractor, B2B service | `references/contract-type-checklists.md` (Employment section) |
| Vendor / supplier / purchase agreement | `references/contract-type-checklists.md` (Vendor section) |
| License agreement / open-source review | `references/ip-and-licensing.md` |

**Always also load** `references/eu-poland-checklist.md` (GDPR, jurisdiction, Polish law applicability apply to nearly everything) and `references/comment-style-guide.md` (writing the comments).

### Step 3 — Analyze

Read the contract end-to-end. For each clause that triggers a checklist item, produce one **finding** with these fields:

```
clause_anchor   : exact phrase in the document to attach the comment to (must appear verbatim)
severity        : DEAL_BREAKER | NEGOTIATE | ACCEPTABLE | INFORMATIONAL
category        : GDPR | IP | LIABILITY | TERMINATION | JURISDICTION | PAYMENT | CONFIDENTIALITY | INDEMNIFICATION | LICENSE | OTHER
comment_pl      : explanation in Polish — what's wrong, why it matters, what the legal basis is
suggested_text  : rewording in the contract's language, OR "—" if no rewording applies
```

**Severity rubric:**
- 🔴 **DEAL_BREAKER** — violates law (e.g., GDPR Art. 28 mandatory clauses missing), exposes the buyer to unlimited liability, gives the vendor unilateral termination with no notice, or assigns away IP the buyer can't afford to lose. Recommend not signing without change.
- 🟠 **NEGOTIATE** — unfavorable but legally OK. Push back, propose alternative wording, but signable if vendor refuses.
- 🟢 **ACCEPTABLE** — standard market clause, flag only so the user knows it's there.
- ⓘ **INFORMATIONAL** — useful context (e.g., "this DPA references SCCs 2021/914 module 2 — appropriate for processor-to-processor"), no action needed.

**Always cover at minimum:**
- Governing law and venue (red-flag anything outside EU/EEA for an EU buyer)
- Liability caps (look for "unlimited liability of Customer" vs "capped liability of Provider" asymmetry)
- IP ownership of Inputs/Outputs (especially for AI services)
- Data-transfer mechanism if non-EEA processor (SCCs? adequacy decision?)
- Termination rights (one-sided convenience termination is a red flag)
- Indemnification scope and exclusions
- Auto-renewal / price increase clauses
- Sub-processor rights and notification
- Audit rights (often absent in vendor paper; sometimes a deal-breaker for regulated buyers)
- Open-source dependencies if mentioned (AGPL is usually a deal-breaker for proprietary products; GPL needs care; MIT/BSD/Apache normally fine)
- Mandatory pre-arbitration / pre-litigation procedures (notice periods, mediation, "good faith negotiation" windows) — usually ACCEPTABLE but always explained, because they delay remedy in clear-breach scenarios
- Mandatory cooperation / information-provision duties from buyer to vendor

**Read clauses for conditional structure, not just substantive content.** Lawyers hide risk in the *condition*, not the *obligation*. Common patterns to flag:

- **"Subject to Customer's compliance with these Terms, [favourable thing for Customer]"** — the favourable thing is now conditional on the buyer never breaching anything. If the favourable thing is IP assignment, license grant, data return, or anything else the buyer genuinely needs, this is at minimum NEGOTIATE: any breach (even an unrelated late payment) can void the buyer's right. Push for: severability of the favourable right from other breaches, or limit the condition to a defined cure-failure event.
- **"To the extent permitted by law, [vendor disclaims/limits something]"** — fine in itself, but note where Polish mandatory law (Art. 473 §2 KC, Art. 449 KC, consumer protections) will override.
- **"As between the parties, [Customer owns X]"** — narrows the ownership statement to a Customer-vs-Vendor allocation, not a statement of universal title. May leave third-party gaps. Worth flagging as INFORMATIONAL.
- **"Provided that..." / "Except that..." / "Notwithstanding..."** — always read the qualifier; it often inverts the main clause's effect.

**Scrutinise vague qualifiers as discretion grants.** When the contract uses any of the following, the qualifier itself is a finding (usually NEGOTIATE, occasionally ACCEPTABLE with explanation):

- "reasonable" / "reasonably" — without an objective benchmark, this is *vendor's reasonableness*. For obligations on the buyer ("reasonable request", "reasonable cooperation"), push for either an objective limit ("to the extent required by law") or a procedural protection ("provided that the request is in writing and specifies the legal basis"). For obligations on the vendor ("reasonable efforts"), push for harder commitment.
- "sole discretion" — flag as red, almost always at least NEGOTIATE.
- "as Anthropic deems necessary" / "as the Provider determines" — same as sole discretion.
- "good faith" — typically uncontroversial under PL law (general principle anyway under Art. 354 KC), but flag if it's the *only* limit on a unilateral power.
- "material" / "materially" — fine if there's a definition or accepted market meaning; problematic if undefined and outcome-determinative.
- "promptly" / "without undue delay" — flag for replacement with a number (24h / 48h / 72h depending on context). Critical for breach notification.
- "from time to time" / "as updated" — when applied to incorporated policies or pricing, this is a unilateral-change right disguised as a temporal phrase.

**Analyse incorporated documents as part of the contract.** When the contract incorporates a Usage Policy, DPA, AUP, Service Specific Terms, Supported Regions Policy, or any other policy by reference:

- These documents are *part of the contract* and must be analysed for substance, not just for the structural risk of unilateral changes.
- For each incorporated policy: fetch its current text (if a URL is provided and the environment has web access) and apply the same checklist analysis.
- Flag findings within those documents the same way as findings in the main contract.
- If the incorporated document is referenced but its text is not available, flag this as a HARD DEPENDENCY in the executive summary: the analysis cannot be considered complete without reviewing the referenced documents, and a follow-up review of those documents is required before signing.

Cross-reference each finding against the loaded checklist files. If a checklist item is **NOT** triggered, do not invent a finding — silence is fine.

### Step 4 — Build executive summary

Compose the summary in Polish. Format as a single document section to prepend to the contract:

```
# Podsumowanie wykonawcze — analiza prawna

**Rekomendacja: PODPISAĆ / NEGOCJOWAĆ / ODRZUCIĆ**

## Liczba ustaleń wg krytyczności
- 🔴 Deal-breakers: N
- 🟠 Do negocjacji: N
- 🟢 Akceptowalne: N
- ⓘ Informacyjne: N

## Najważniejsze deal-breakery
1. [Tytuł problemu] — sekcja X.Y
   [2–3 zdania: co dokładnie jest nie tak, dlaczego to zagraża kupującemu, jaka jest podstawa prawna lub rynkowy benchmark.]
2. [Tytuł problemu] — sekcja X.Y
   [2–3 zdania: opis problemu, konsekwencje, uzasadnienie.]
3. ...

## Checklist zgodności
- GDPR / RODO: ✅ / ❌ / ⚠️ (z notatką)
- Prawo własności intelektualnej: ...
- Jurysdykcja i prawo właściwe: ...
- Ograniczenie odpowiedzialności: ...
- Rozwiązanie umowy: ...
- Transfer danych poza EOG: ... (jeśli dotyczy)

## Uwagi ogólne
[2–4 zdania — strategiczna ocena, np. „Umowa typowa dla amerykańskiego dostawcy SaaS; główne ryzyko to ograniczenie odpowiedzialności do 12 miesięcy opłat oraz brak prawa audytu."]

## Weryfikacja źródeł
Analiza opiera się na następujących źródłach (zweryfikowanych dn. <YYYY-MM-DD>):
- [lista konkretnych zweryfikowanych źródeł — np. „RODO, tekst skonsolidowany EUR-Lex"; „SCC 2021/914 — status obowiązujący"; „Wytyczne EDPB 04/2021"]
- [jeśli weryfikacja jakiegoś punktu była niejednoznaczna — zaznaczyć]
```

### Step 5 — Assemble the markdown report

Write `<original_name>_legal_review.md` in the working/output directory: the executive summary (Step 4) first, then every finding in document order using the findings format from "Output format at a glance". This is the primary deliverable — always produce it.

### Step 5b — Annotated .docx (only when the user asks for a Word file)

Use the bundled `scripts/docx_tool.py` (Python 3 stdlib only):

1. **Get an annotation base.** If the source was a `.docx`, use the original file directly. Otherwise build one from the full contract text (preserve ALL sections, numbering, and headings; markdown headings `#`–`####` become styled headings):
   ```bash
   python3 scripts/docx_tool.py create contract_full.md working.docx
   ```
2. **Write `summary.md`** — the Polish executive summary from Step 4 (markdown; `**bold**`, `#` headings, and `-` bullets are rendered).
3. **Write `findings.json`** — plain text in JSON, no XML escaping needed:
   ```json
   {"author": "Legal Risk Skill", "initials": "LR", "summary": "summary.md",
    "findings": [
      {"anchor": "<clause text appearing verbatim in the document>",
       "comment": "[🔴 DEAL-BREAKER | KATEGORIA: GDPR]\n<Polish explanation>\n\nSugerowana zmiana (do wklejenia):\n\"<replacement wording in contract language>\""}
    ]}
   ```
4. **Run:**
   ```bash
   python3 scripts/docx_tool.py annotate working.docx findings.json <original_name>_legal_review.docx
   ```
5. The script prepends the summary as page 1 and anchors each comment to the paragraph containing its `anchor`. Unmatched anchors are listed on stderr (exit code 2) — fix them and re-run. If an anchor phrase appears multiple times, use a longer surrounding string.

If Python 3 is unavailable or the script fails irrecoverably, deliver the markdown report and tell the user why the .docx couldn't be produced.

### Step 6 — Deliver

1. Save the deliverable(s) in the working/output directory and give the user the exact file path(s) (use the environment's file-presentation mechanism if one exists).
2. In the chat reply, give a **brief** verbal summary (3–5 sentences): the overall recommendation, the count of deal-breakers, and one sentence on the biggest risk. Do not re-explain everything — the document does that.

---

## Critical rules

- **Verify before citing.** Any comment that cites a specific legal authority (article number, regulation, deadline, named decision) must be backed by a verification search in this session. See `references/sources-and-verification.md` for sources and protocol. If verification is inconclusive, soften the language — don't invent certainty.
- **Always Polish for comments, contract-language for suggested rewording.** Never mix them. If the contract is in Polish, suggested rewording is also in Polish.
- **Always assume the user is the buyer.** Frame everything from the buyer's perspective: which clauses harm THEM, which protections are missing for THEM. Flip the analysis if the user explicitly says otherwise.
- **EU/Poland is the home jurisdiction.** Anything that forces the user into a non-EU forum, non-EU governing law, or non-EEA data processing without SCCs is at minimum a NEGOTIATE finding, often DEAL_BREAKER.
- **Never give "this is/isn't legal advice" disclaimers in the output.** The user knows. Don't pad the comments.
- **Don't invent findings to look thorough.** A clean clause gets no comment. Quality over quantity.
- **Don't quote more than 15 words verbatim from the contract** in any single comment — paraphrase. (Copyright safety.)
- **The clause_anchor text must appear verbatim and unambiguously** in the document — in the markdown report it lets the user find the clause; in .docx mode the comment won't attach without it. If a phrase appears multiple times, use a longer surrounding string.
- **ALWAYS cover the full original document.** Analyze every section; in .docx mode the output must contain every paragraph of the original — not just clauses with findings. Creating a partial document with only commented paragraphs is a critical failure mode.
- **Never assume platform-specific tools or paths.** Use only relative paths, the bundled `scripts/docx_tool.py`, and capabilities the current environment actually exposes.

---

## Bundled script

- `scripts/docx_tool.py` — stdlib-only Python 3 helper: `extract` text from a .docx, `create` a .docx from markdown-ish text, `annotate` a .docx with Word comments + prepended executive summary. Run `python3 scripts/docx_tool.py` for usage.

## Reference files

- `references/sources-and-verification.md` — Authoritative legal sources, verification protocol, and rules about when to web-search before citing authority. **Load this first, before analysis.**
- `references/eu-poland-checklist.md` — GDPR/RODO, Polish Civil Code, jurisdiction, cross-border issues, Schrems II
- `references/ip-and-licensing.md` — IP assignment, open-source licenses (MIT/GPL/AGPL/Apache/BSD/etc.), copyright, patent, trademark
- `references/contract-type-checklists.md` — Per-contract-type checklist of what to look for (T&C, DPA, NDA, SaaS, employment, vendor)
- `references/comment-style-guide.md` — How to write the Polish comments (tone, format, severity tags, example phrasings)
