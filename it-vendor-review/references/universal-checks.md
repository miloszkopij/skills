# Universal Checks — Every IT Contract

These items must be reviewed in **every** IT vendor contract, regardless of type.

---

## 1. Limitation of Liability (LoL)

**What to look for:**
- Cap amount — typical vendor offer: 12 months of fees. Acceptable: 12–24 months. Below 3 months: 🔴 CRITICAL.
- Mutual vs. one-sided cap — if vendor caps their liability but buyer's liability is uncapped: 🔴 CRITICAL.
- Exclusion of consequential/indirect damages — standard but dangerous if combined with low cap. Flag if both apply simultaneously: 🟠 HIGH.
- Carve-outs from the cap — IP indemnification, GDPR breaches, death/personal injury, willful misconduct should be carved out. If absent: 🟠 HIGH.
- Data breach liability — vendor often caps it at the LoL amount, but buyer's exposure to third parties (customers, UODO fines) is uncapped. Flag this asymmetry: 🟠 HIGH.

**Benchmark:** Cap ≥ 12 months fees with data breach and GDPR carve-out = acceptable.

---

## 2. Indemnification

**What to look for:**
- IP infemnification — vendor should indemnify buyer if the product infringes third-party IP. If absent or limited to specific geographies only: 🟠 HIGH.
- Carve-outs that gut IP indemnity — "indemnity void if buyer modifies the software" or "void if used in combination with other software" — standard but can be broad: 🟡 MEDIUM.
- Feedback/residuals clauses — vendor can use ideas you share as improvements. Often buried. Flag: 🟠 HIGH.
- Open-source components — if product contains OSS under GPL/LGPL/AGPL, buyer may have obligations. Absent disclosure: 🟠 HIGH.
- One-sided indemnity — buyer indemnifies vendor broadly but vendor's indemnity is narrow: 🟠 HIGH.

---

## 3. Governing Law and Jurisdiction

**What to look for:**
- Non-EU governing law (especially US state law): 🟠 HIGH for Polish buyer — may conflict with GDPR, Polish consumer/civil code rights.
- Exclusive non-EU jurisdiction (e.g., Delaware courts): 🟠 HIGH — practical impossibility of enforcement.
- Arbitration-only clause with a foreign seat: 🟠 HIGH.
- No choice of law — defaults to vendor's domicile law: 🟡 MEDIUM.

**Benchmark:** EU governing law (any member state) + EU forum = ✅. US law + EU dispute resolution = negotiable. US law + US courts = 🟠.

---

## 4. Termination Rights

**What to look for:**
- Termination for convenience (buyer) — should exist with reasonable notice (30–90 days): absent = 🟠 HIGH.
- Termination for cause — should be triggered by repeated SLA failure, not just material breach. Vague "material breach" standard: 🟡 MEDIUM.
- Cure period for buyer too long — 30 days is standard; 60–90 days delays buyer's right to exit: 🟡 MEDIUM.
- Vendor termination rights very broad — e.g., "vendor can suspend/terminate for convenience with 30 days notice": 🟠 HIGH if production-critical.
- Termination for non-payment — standard, but check: does one missed payment allow immediate termination? Should require cure period: 🟡 MEDIUM.
- Auto-renewal — notice period >90 days to prevent renewal: 🔴 CRITICAL (operational trap). 30–60 days: 🟡 MEDIUM. 90 days: 🟡 MEDIUM.

---

## 5. Price Change Rights

**What to look for:**
- Unilateral price increases — vendor can increase price on X days notice: flag with how many days and whether buyer can exit: 🟠 HIGH if no exit right.
- Annual price escalation cap — uncapped annual increases: 🟠 HIGH. CPI-linked cap: acceptable. >10% annual cap: 🟡 MEDIUM.
- "Pricing subject to change" incorporated by reference to a URL: 🔴 CRITICAL — this is a blank check.
- Overage charges — consumption-based pricing without a notification or cap mechanism: 🟠 HIGH.

---

## 6. Confidentiality

**What to look for:**
- Residuals clause — information retained in employee memory can be used: 🟠 HIGH for IP-sensitive buyers.
- Duration — "during the agreement only" with no post-term confidentiality: 🟠 HIGH. 3–5 years post-term: acceptable. Perpetual: ideal.
- Vendor right to use buyer data for product improvement / AI training: 🟠 HIGH — see also gdpr-and-data.md.
- No confidentiality provision at all: 🔴 CRITICAL.

---

## 7. Force Majeure

**What to look for:**
- Cloud provider outages classified as force majeure — vendor chose AWS/Azure/GCP; their infra failures should not be vendor's force majeure: 🟠 HIGH.
- Pandemic/cyberattack as force majeure — cyberattack on vendor is their risk to manage; if it voids SLA: 🟠 HIGH.
- Force majeure excuses payment obligations — very unusual and unacceptable: 🔴 CRITICAL.
- No SLA credit during force majeure — i.e., downtime doesn't count against SLA even if it's vendor's infrastructure failure: 🟠 HIGH.

---

## 8. Assignment

**What to look for:**
- Vendor can assign contract without buyer consent — in M&A, buyer's vendor becomes unknown entity: 🟠 HIGH. Should require consent or termination right.
- Change of control clause — if vendor is acquired, buyer should have exit right: absent = 🟠 HIGH.
- Buyer cannot assign to subsidiaries/group companies: 🟡 MEDIUM — may block internal restructuring.

---

## 9. Audit Rights

**What to look for:**
- Vendor has audit rights on buyer's usage (license audit) — check scope, notice requirements, and who pays for the audit: 🟡 MEDIUM baseline; 🟠 HIGH if audit costs fall on buyer.
- Buyer has no audit/inspection rights on vendor's security posture or SLA measurement data: 🟠 HIGH for production-critical.
- Vendor can audit on short notice (e.g., 3 days) — industry standard is 30 days: 🟡 MEDIUM.

---

## 10. Dispute Resolution

**What to look for:**
- Mandatory arbitration — check: is it in addition to or instead of court? Arbitration fees can be expensive: 🟡 MEDIUM.
- No escalation procedure before litigation/arbitration: 🟡 MEDIUM.
- Expert determination for technical disputes — appropriate; check whether decision is binding: ⓘ.
- Injunctive relief carve-out — vendor can seek injunctive relief (e.g., to stop IP infringement) without arbitration: acceptable, ⓘ.

---

## 11. Entire Agreement / Incorporation by Reference

**What to look for:**
- Policies incorporated by reference (AUP, Privacy Policy, SLA document, pricing schedule) — these are part of the contract. Must be reviewed. Flag as 🟠 HIGH if unavailable.
- "As updated from time to time" applied to incorporated policies — vendor can unilaterally change AUP/SLA without contract amendment: 🔴 CRITICAL.
- Order of precedence — if conflicts between main contract and incorporated policies, which wins? Unclear hierarchy: 🟡 MEDIUM.

---

## 12. Notices

**What to look for:**
- Notices only to a physical address — email notice not valid: 🟡 MEDIUM (practical issue for time-sensitive termination notices).
- Very short notice periods for important vendor actions (suspension, termination): 🟡 MEDIUM.
