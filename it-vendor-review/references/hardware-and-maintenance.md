# Hardware Supply and Maintenance Checks

---

## 1. Hardware Supply Contract — Core Risks

**Specification and acceptance:**
- Specifications vague — "equivalent or similar hardware": 🟠 HIGH. Must be specific make/model/spec.
- No acceptance testing procedure — delivery = acceptance: 🟠 HIGH. Push for formal UAT/ATP.
- Acceptance period too short (< 5 business days): 🟡 MEDIUM.
- Risk transfers to buyer on delivery, not on acceptance: 🟠 HIGH.
- No incoming inspection right — buyer cannot reject damaged goods after signing delivery receipt: 🟠 HIGH.

**Warranty:**
- Warranty period < 12 months (industry standard for hardware): 🟡 MEDIUM. Enterprise hardware: 3–5 years with extended warranty.
- Warranty excludes damage from "normal use" or "environmental conditions" without precise definition: 🟡 MEDIUM.
- Warranty void if buyer opens equipment or uses non-OEM parts: check against buyer's actual practices.
- Return process — RMA required, buyer pays shipping: 🟡 MEDIUM.

---

## 2. Hardware Maintenance SLA — Benchmarks

**On-site response times (industry benchmarks):**

| Coverage | Response time | Verdict |
|---|---|---|
| 24/7 x 4-hour on-site | 4h response, engineer on-site | ✅ Gold standard for critical infra |
| NBD (Next Business Day) | By next business day | ✅ Acceptable for non-critical |
| 8x5 NBD | Business hours only, next day | 🟡 MEDIUM for production hardware |
| Best effort | Undefined | 🔴 CRITICAL |

**Flag:**
- No on-site SLA — only remote/phone support for hardware that requires physical intervention: 🟠 HIGH.
- "Best effort" parts availability — critical if rare components: 🟠 HIGH.
- Parts stocking commitment absent — vendor may need to order parts internationally: 🟡 MEDIUM. Push for regional parts depot.
- Loaner/replacement equipment during repair absent: 🟡 MEDIUM for business-critical hardware.
- Response time measured from ticket open, not from vendor acknowledgement: 🟡 MEDIUM.

---

## 3. End of Life (EOL) / End of Support (EOS)

**Flag:**
- Vendor sells hardware that is already or nearly EOL (< 24 months to EOL): 🟠 HIGH. Maintenance contract may not outlast the hardware.
- No EOL notification obligation — vendor can announce EOL with < 12 months notice: 🟠 HIGH.
- Post-EOL maintenance not offered or very expensive: 🟡 MEDIUM — plan migration costs.
- Spare parts availability commitment post-EOL absent: 🟡 MEDIUM.
- Firmware/security updates end at EOL — security risk for any internet-connected hardware: 🟠 HIGH.

---

## 4. Maintenance Contract Scope

**Flag:**
- PM (Preventive Maintenance) visits — check frequency commitment. Absent: 🟡 MEDIUM.
- Excluded failure types — "damage from power surges" excluded: 🟡 MEDIUM (push for clear exclusion list).
- Software/firmware updates included in maintenance? Absent specification: 🟡 MEDIUM.
- Configuration management — who is responsible for configuration backup before maintenance? Absent: 🟡 MEDIUM.
- Third-party component coverage — e.g., if server contains 3rd-party drives, are they covered? Absent: 🟡 MEDIUM.

---

## 5. Escalation and Replacement

**Flag:**
- No escalation path if repair takes longer than SLA: 🟠 HIGH.
- No hardware replacement commitment if same fault recurs (e.g., 3+ times in 12 months): 🟠 HIGH. Push for chronic-failure replacement clause.
- Repaired-with-refurbished-parts policy — buyer receives refurbished parts as replacement: 🟡 MEDIUM. Negotiate new-for-new on warranty period.
- Root cause analysis (RCA) not required after critical failures: 🟡 MEDIUM.

---

## 6. Hardware Pricing — Escalation and True-Up

**Flag:**
- Maintenance price escalation uncapped — annual increases without exit right: 🟠 HIGH.
- Spare parts priced at "current list price" at time of incident — not fixed: 🟡 MEDIUM. Push to lock parts pricing.
- Additional site coverage not in base price — expanding to new office requires renegotiation: 🟡 MEDIUM. Clarify.
- Time and materials billing for out-of-scope work — check what is "out of scope": 🟡 MEDIUM.
