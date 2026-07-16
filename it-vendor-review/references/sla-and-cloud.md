# SLA and Cloud Checks — SaaS / Cloud / Hosted Services

The most operationally dangerous section of any SaaS or cloud contract. Read every SLA clause with math, not just legal language.

---

## 1. Uptime Commitment — Benchmarks

| Uptime % | Downtime/month | Verdict for production |
|---|---|---|
| 99.9% ("three nines") | ~43 min/month | ✅ Minimum acceptable for non-critical |
| 99.5% | ~3.6 hours/month | 🟠 HIGH for production use |
| 99% | ~7.3 hours/month | 🔴 CRITICAL for any production use |
| "best efforts" / "commercially reasonable" | undefined | 🔴 CRITICAL — not an SLA |
| No uptime stated | — | 🔴 CRITICAL |

**For business-critical / revenue-critical systems:** minimum acceptable is 99.95% (~22 min/month). 99.99% ("four nines") = ~4.4 min/month; ask for it.

**Flag immediately:**
- "Uptime" undefined — does it include scheduled maintenance? It shouldn't.
- Measurement window — monthly is standard. Annual measurement means one bad month can be hidden by 11 good months: 🟠 HIGH.
- Vendor measures uptime themselves — no third-party verification possible: 🟡 MEDIUM. Push for independent monitoring right.

---

## 2. Exclusions from SLA Measurement

Common exclusions — evaluate each:

| Exclusion | Verdict |
|---|---|
| Scheduled maintenance windows (pre-notified, ≤ 4h/month) | ✅ Acceptable |
| Emergency maintenance | 🟡 MEDIUM — require notification obligation |
| Buyer's network/ISP failures | ✅ Acceptable |
| Third-party service failures (APIs, CDNs vendor chose) | 🔴 CRITICAL — vendor's architectural choices are vendor's risk |
| Cloud provider outages (AWS/Azure/GCP) | 🔴 CRITICAL — same as above |
| Force majeure | 🟠 HIGH — see universal-checks.md |
| "Beta" or "preview" features | 🟡 MEDIUM — check if buyer actually uses them in production |
| Any factor "beyond vendor's reasonable control" — vague | 🔴 CRITICAL — blanket exclusion |

---

## 3. SLA Credit Formula — Do the Math

**Red flags in credit structures:**

- Credits are the **only** remedy — buyer cannot terminate or claim damages even after chronic failure: 🟠 HIGH. Require termination right after repeated breach (e.g., 3 months in 6 with SLA failure).
- Credit cap at 10–15% of monthly fee — on a 10,000 EUR/month contract, a complete outage yields 1,000–1,500 EUR credit. This is almost never worth the downtime cost: 🟠 HIGH.
- Credit cap at 1 monthly fee — slightly better but still likely insufficient for business-critical systems: 🟡 MEDIUM.
- Credit requires a **claim** — buyer must proactively submit a ticket within X days to receive credit. Missed deadline = no credit: 🟠 HIGH. Push for automatic credits.
- Credit applied to **future invoice** only — if buyer terminates, credits are lost: 🟡 MEDIUM.
- "Service credits are Customer's sole and exclusive remedy" — eliminates any other legal recourse for downtime: 🔴 CRITICAL for production-critical buyers.

**Calculate real exposure:** Take the contract monthly value × downtime % exposure × actual credit formula. State in EUR/PLN if possible. Example: "Na kontrakt 50 000 PLN/mies., 2h przestoju = credit ok. 2 500 PLN, podczas gdy koszt przestoju szacowany na 10× więcej."

---

## 4. Support SLA — Response and Resolution Times

**Benchmark tiers (industry standard for B2B SaaS):**

| Priority | Definition | Target response | Target resolution |
|---|---|---|---|
| P1 / Critical | Production down, all users affected | ≤ 1 hour | ≤ 4 hours |
| P2 / High | Major function unavailable, workaround exists | ≤ 4 hours | ≤ 24 hours |
| P3 / Medium | Degraded performance, workaround available | ≤ 8 hours (business hours) | ≤ 72 hours |
| P4 / Low | Minor issue, cosmetic | ≤ 2 business days | Best effort / next release |

**Flag:**
- Response time ≥ 4 hours for P1: 🟠 HIGH.
- Response is automated acknowledgement (not human engineer): 🔴 CRITICAL. Contract must say "qualified engineer acknowledgement."
- Support only during business hours (no 24/7 for P1): 🟠 HIGH for production-critical.
- No resolution time committed (response time only): 🟠 HIGH.
- Priority levels defined by vendor unilaterally — vendor can reclassify P1 as P3: 🟠 HIGH. Require joint classification or dispute mechanism.
- No escalation path defined: 🟡 MEDIUM.

---

## 5. Maintenance Windows

**Flag:**
- Unscheduled maintenance — vendor can perform maintenance without notice: 🟠 HIGH.
- Notice period < 48 hours for scheduled maintenance: 🟡 MEDIUM (industry standard: 5–7 business days for planned, 24h for urgent).
- Maintenance windows during business hours (09:00–17:00 buyer timezone) without buyer consent: 🟠 HIGH.
- No maintenance window calendar / excessive frequency: 🟡 MEDIUM.

---

## 6. Cloud Vendor Lock-In

**Flag:**
- Proprietary data formats with no export function: 🔴 CRITICAL.
- Data export only in non-standard formats (vendor-specific JSON schema, binary exports): 🟠 HIGH.
- Data export fees — charging per GB for data retrieval upon termination: 🟠 HIGH.
- Egress bandwidth charges — not stated in contract, subject to cloud pricing: 🟠 HIGH. Require a cap or include in contract price.
- No data return timeline — after termination, how long until buyer's data is accessible for export? Absent: 🟠 HIGH. Benchmark: 30–90 days post-termination.
- Data deletion — after return window, vendor should delete all buyer data (including backups). No deletion commitment: 🟠 HIGH (GDPR issue too — see gdpr-and-data.md).
- API deprecation — vendor can deprecate APIs with 30 days notice: 🟡 MEDIUM. Push for 90–180 days + compatibility layer.

---

## 7. Disaster Recovery and Business Continuity

**What to look for:**
- RTO (Recovery Time Objective) not stated: 🟠 HIGH for production-critical.
- RPO (Recovery Point Objective) not stated — how much data can be lost in a disaster: 🟠 HIGH.
- Backup frequency not stated: 🟡 MEDIUM. Benchmark: daily minimum, hourly for critical data.
- DR environment not in EU if buyer requires EU data residency: 🟠 HIGH (GDPR issue if personal data).
- Vendor has no DR plan or hasn't tested it within 12 months: 🟠 HIGH — ask for evidence.

**Benchmarks:**
| Criticality | RTO | RPO |
|---|---|---|
| Mission-critical | ≤ 4 hours | ≤ 1 hour |
| Business-critical | ≤ 24 hours | ≤ 4 hours |
| Standard | ≤ 72 hours | ≤ 24 hours |

---

## 8. Multi-tenancy and Isolation

**Flag:**
- No statement of logical isolation between tenants: 🟡 MEDIUM.
- Shared infrastructure (database, compute) with no isolation guarantee: 🟠 HIGH for regulated data.
- "Noisy neighbor" risk — no performance isolation guarantee: 🟡 MEDIUM.
- No mention of security certifications (SOC 2 Type II, ISO 27001): 🟠 HIGH for any service processing personal or sensitive data.

---

## 9. Price Escalation in Cloud/SaaS

**Flag:**
- Consumption-based pricing with no cap — usage spikes = unbounded cost: 🟠 HIGH. Require spend alerts and hard caps.
- Per-user pricing with "true-up" — additional users auto-billed at contract rate: 🟡 MEDIUM.
- Storage overage pricing not in contract — subject to "current rate card": 🟠 HIGH.
- Annual price increase without exit right — vendor can raise 15% per year with 60 days notice, no buyer exit right: 🔴 CRITICAL.
- Feature removal — vendor can remove features mid-contract: 🟠 HIGH. Should trigger renegotiation or exit right.
