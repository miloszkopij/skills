# Software Licensing Checks

---

## 1. License Scope — What You Can Actually Do

**Flag:**
- Named-user vs. concurrent user — if contract says "named user" but buyer expects concurrent sharing: 🔴 CRITICAL.
- Device-based licensing — license tied to specific hardware; can't deploy on new machines without repurchase: 🟡 MEDIUM.
- Use restrictions — "for internal use only," "non-commercial only," "for [specific business unit] only": assess against actual planned use. Mismatch: 🔴 CRITICAL.
- Virtualization prohibited without additional license — very common in enterprise software (Oracle, SAP): 🔴 CRITICAL. Check if buyer uses VMs.
- Cloud deployment prohibited — on-premise license cannot be run in a cloud VM: 🔴 CRITICAL.
- No sublicensing to subsidiaries / group companies: 🟡 MEDIUM — may block group-wide deployment.
- Geographic restrictions: 🟠 HIGH if buyer operates across multiple countries.

---

## 2. License Audit Rights

**Flag (extremely common danger in enterprise software):**
- Vendor can audit buyer's installations — this is standard but the terms matter enormously.
- Audit notice period < 30 days: 🟡 MEDIUM. Push for 60 days.
- Audit more than once per 12-month period without cause: 🟠 HIGH.
- Audit costs fall on buyer — especially if "shortfall is found": 🟠 HIGH. Should be vendor's cost unless >5% underpayment.
- Audit results shared with third parties (e.g., vendor's reseller): 🟠 HIGH.
- Audit covers historical periods > 2 years: 🟡 MEDIUM.
- True-up pricing at current list price — not contracted price: 🔴 CRITICAL. Any shortfall should be billed at contracted discount rates.
- Self-reporting requirement — buyer must proactively report overuse: 🟡 MEDIUM — ensure internal tracking processes exist.

**Audit trap pattern to flag:** Perpetual license + broad audit rights + true-up at list price + no cap on back-billing = Oracle-style audit risk. Call this out explicitly.

---

## 3. Perpetual vs. Subscription

**Perpetual license:**
- What happens to license if vendor is acquired / goes bankrupt? Should be "license survives": absent = 🟠 HIGH.
- Maintenance/support renewal — can vendor refuse to provide support for older versions (EOL/EOS)? Check timeline: 🟡 MEDIUM.
- Source code escrow — if vendor fails, buyer can access source code to maintain the software. Absent for business-critical perpetual software: 🟠 HIGH.
- Version lock — license only covers current version; future versions require upgrade purchase: clarify.

**Subscription:**
- What happens to buyer's data if subscription lapses / is terminated? Data return window: absent = 🟠 HIGH.
- Downgrade rights — if buyer reduces seats mid-term, can they? Usually not. Evaluate against buyer's scaling plans.

---

## 4. Open Source Components

**Flag:**
- No disclosure of open source components used in the product: 🟡 MEDIUM.
- AGPL/GPL components — "copyleft" licenses may impose obligations if buyer modifies or distributes. Absent disclosure: 🟠 HIGH.
- Vendor indemnity explicitly excludes open source components: 🟠 HIGH — OSS IP risk falls entirely on buyer.
- No SBOM (Software Bill of Materials) — increasingly expected for enterprise and regulated use: 🟡 MEDIUM.

---

## 5. Updates, Upgrades, and Versioning

**Flag:**
- Vendor can change features/APIs in minor updates without notice: 🟡 MEDIUM.
- Major version upgrades are a separate purchase — not included in maintenance: clarify; 🟡 MEDIUM if buyer expects them.
- Vendor can end-of-life (EOL) current version with < 12 months notice: 🟠 HIGH.
- Security patches only provided for current version — forces upgrades buyer may not be ready for: 🟡 MEDIUM.
- No LTS (Long-Term Support) option available: 🟡 MEDIUM for buyers with slow upgrade cycles.

---

## 6. Ownership of Customizations and Integrations

**Flag:**
- Buyer builds customizations/integrations on vendor platform — who owns the IP? Absent: 🟠 HIGH.
- Vendor claims joint ownership of buyer's integrations: 🔴 CRITICAL.
- Customizations cannot be transferred if buyer switches vendors: 🟠 HIGH.
- Vendor's "feedback" clause — buyer's suggested improvements become vendor's IP: 🟠 HIGH.

---

## 7. License Transferability and Exit

**Flag:**
- License is non-transferable — buyer cannot transfer to successor entity in M&A: 🟠 HIGH.
- No portability to alternative hosting/delivery: 🟡 MEDIUM.
- Migration assistance from vendor not guaranteed: 🟡 MEDIUM for complex integrations.
