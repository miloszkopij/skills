# Managed Services (MSP / NOC / SOC / Helpdesk) Checks

---

## 1. Scope of Services

**Flag:**
- Service scope vague — "IT support as agreed" without a detailed Statement of Work (SOW): 🔴 CRITICAL.
- No device/system coverage list — what exactly is covered: 🟠 HIGH.
- "Best effort" support without defined response/resolution times: 🔴 CRITICAL.
- Out-of-scope work pricing undefined — ad-hoc T&M rate not agreed in contract: 🟡 MEDIUM. Risk: scope creep billed at premium rates.
- No change management process defined — vendor can claim any request is "out of scope": 🟠 HIGH.

---

## 2. Helpdesk / Incident Response SLA

Use the same benchmarks as sla-and-cloud.md (P1–P4). Additional MSP-specific flags:

- No distinction between incident and service request SLA: 🟡 MEDIUM.
- SLA for remote support only; on-site SLA undefined: 🟠 HIGH if physical presence needed.
- On-site SLA: check geographic coverage and travel time clauses. Regional office not covered: 🟡 MEDIUM.
- SLA clock starts at ticket open, not at incident occurrence: 🟡 MEDIUM — buyer must self-detect and report.

---

## 3. Shared Responsibility

**Flag (this is where most disputes originate):**
- No RACI or responsibility matrix: 🟠 HIGH.
- Dependency failures — if buyer's network is down and MSP can't respond, what happens? Absent: 🟠 HIGH.
- Vendor can blame buyer's environment for SLA non-compliance without a defined dispute mechanism: 🟠 HIGH.
- Security incidents — if a breach occurs, who leads the response? Absent: 🔴 CRITICAL.
- Third-party vendor coordination (ISP, cloud provider) — who manages them? Absent: 🟡 MEDIUM.

---

## 4. Staffing and Key Personnel

**Flag:**
- No minimum staffing commitment — vendor can reduce headcount without notice: 🟠 HIGH.
- Key person dependency without substitution plan — one engineer knows all buyer systems: 🟠 HIGH.
- Subcontracting to unnamed third parties permitted without buyer consent: 🟠 HIGH.
- Staff turnover — high turnover at MSP causes knowledge loss. No knowledge transfer obligation: 🟡 MEDIUM.
- Background checks not required for staff accessing buyer systems: 🟠 HIGH.

---

## 5. Reporting and Visibility

**Flag:**
- No regular service reporting obligation: 🟠 HIGH. Minimum: monthly SLA performance report.
- No access to ticketing system data / audit trail: 🟡 MEDIUM.
- SLA measurement done exclusively by vendor — no independent verification: 🟡 MEDIUM.
- Incident root cause analysis (RCA) not required for P1/P2 incidents: 🟡 MEDIUM. Push for RCA within 48–72h.
- No capacity/performance trend reporting: ⓘ.

---

## 6. Security Obligations

**Flag:**
- MSP has broad access to buyer systems — no privileged access management (PAM) requirement: 🟠 HIGH.
- Credentials shared via email/chat — no secure vault requirement: 🟠 HIGH.
- No requirement for MFA for MSP staff accessing buyer systems: 🟠 HIGH.
- Audit log of all MSP actions on buyer systems not required: 🟠 HIGH.
- MSP's own security posture not warranted — no ISO 27001 / SOC 2 requirement: 🟠 HIGH.
- Breach caused by MSP — liability limited to monthly fee cap: 🔴 CRITICAL.

---

## 7. Transition In / Out

**Transition in:**
- No knowledge transfer obligation at contract start: 🟡 MEDIUM.
- Due diligence / discovery phase not included in price: 🟡 MEDIUM.

**Transition out:**
- No exit transition assistance: 🟠 HIGH. Push for minimum 90-day transition assistance at no extra charge.
- Exit assistance priced at premium rates: 🟡 MEDIUM.
- Documentation — vendor must provide up-to-date runbooks, network diagrams, asset inventory: absent = 🟠 HIGH.
- Credentials and access — all credentials, certificates, and keys must be returned at termination: absent = 🔴 CRITICAL.
- Knowledge transfer to successor vendor not required: 🟠 HIGH.
