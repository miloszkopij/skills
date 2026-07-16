# Sub-processor Analysis Framework

Detailed guidance for Step 4 of the DPA Analyzer.

---

## Models of sub-processor authorisation

### Model A — Specific authorisation (most buyer-friendly)
Each sub-processor requires explicit written approval from the controller. Rare in standard vendor DPAs but best for high-sensitivity processing.
→ 🟢 ACCEPTABLE — flag as favourable to buyer.

### Model B — General written authorisation (market standard)
GDPR Art. 28(2) permits this. Vendor maintains a list; controller has approved the list in principle by signing the DPA; changes require notice + right to object.
→ 🟢 ACCEPTABLE if all of the below are present.

### Model C — No authorisation mechanism
Vendor can change sub-processors freely.
→ 🔴 DEAL-BREAKER — explicit GDPR violation.

---

## Required elements for Model B (general authorisation)

### 1. Current sub-processor list
- Published at a URL, or attached as Annex
- Must include: name, location, processing activity
- "We work with reputable third-party providers" → 🔴 (not a list)
- URL provided but not accessible → 🟠 (flag, verify at time of signing)

### 2. Notice of new sub-processors
| Notice period | Severity |
|---|---|
| ≥ 30 calendar days | 🟢 |
| 14–29 days | 🟠 |
| < 14 days | 🟠 → 🔴 if processing is critical |
| None | 🔴 |

### 3. Right to object
- Controller must be able to object to a new sub-processor
- If objection sustained → contractual exit without penalty
- "Vendor will consider objections in good faith" without exit right → 🟠
- No right to object at all → 🔴

Suggested language:
> "Provider shall give Controller at least thirty (30) days' prior written notice of any intended changes to its sub-processor list. Controller may reasonably object to such changes within fifteen (15) days of notice. If the parties cannot resolve the objection, Controller may terminate the affected Services within thirty (30) days of notice without penalty, subject to pro-rata refund of prepaid fees."

### 4. Art. 28(4) flowdown obligation
Vendor must impose Art. 28(3) obligations on sub-processors by contract.
- Explicit flowdown obligation → 🟢
- "Sub-processors are contractually bound to appropriate standards" → 🟠 (vague; push for explicit Art. 28(4) reference)
- No flowdown provision → 🔴

---

## Sub-processor chains and EEA exits

For each sub-processor outside the EEA, ask: what transfer mechanism covers that hop?

Common sub-processor EEA-exit scenarios:
| Scenario | Transfer mechanism needed |
|---|---|
| Vendor (EU) → sub-processor (US) | Module 3 SCCs (processor → processor) OR sub-processor DPF-certified |
| Vendor (US) → sub-processor (US) | Module 3 SCCs embedded in sub-processor agreement; or DPF covers sub-processor too |
| Vendor (EU) → sub-processor (India, Brazil, etc.) | Module 3 SCCs; check adequacy status of country |

If the DPA only covers the controller → vendor transfer (Module 2) but is silent on sub-processor onward transfers:
→ 🟠 NEGOTIATE — push for explicit coverage of sub-processor transfer mechanisms.

---

## Multi-entity concern: sub-processor authorisation scope

If supporting entities are co-controllers under the same DPA:
- Does the general authorisation extend to processing initiated by supporting entities?
- Does the sub-processor list cover all data flows from all group entities?
- If supporting entities are in different Member States: does the DPA cover cross-border intra-group processing?

If the DPA is silent on group-entity sub-processor coverage: 🟠 — push to extend the authorisation clause explicitly to Affiliates.

---

## AI/ML services — special sub-processor concern

If the vendor's service uses AI/ML infrastructure:
- GPU cloud providers (AWS, Azure, GCP, CoreWeave, etc.) are typically sub-processors
- Training infrastructure sub-processors need to be named — "cloud infrastructure" is not a name
- If the vendor uses foundation model providers (OpenAI API, Anthropic API, Google Gemini API, etc.) these are sub-processors and must be listed
- Model training on customer data: even if the vendor disclaims it, verify that the sub-processor agreement with the model provider also restricts training use

Flag as 🟠 if AI sub-processor list appears incomplete given the nature of the service.
