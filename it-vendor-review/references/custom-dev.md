# Custom Software Development Checks

---

## 1. Scope and Requirements

**Flag:**
- SOW/specification is high-level with no detailed acceptance criteria: 🔴 CRITICAL — "project delivered when vendor says so."
- Requirements subject to vendor's interpretation: 🟠 HIGH.
- Change control process not defined — changes handled "collaboratively": 🟠 HIGH. All scope changes must be documented and priced in writing.
- Vendor estimates are non-binding — final price TBD: 🟠 HIGH for fixed-budget projects.

---

## 2. Intellectual Property Ownership

**Flag (most critical issue in custom dev):**
- IP vests in vendor by default — buyer gets only a license: 🔴 CRITICAL. Buyer paid for development; buyer should own the IP.
- IP assignment requires separate assignment deed at end — if vendor goes bankrupt, IP transfer may not complete: 🟠 HIGH. Require automatic IP vesting on creation/payment.
- Work-for-hire doctrine applied — check if applicable under Polish law (generally, Kodeks pracy applies to employees, not B2B contractors): requires specific assignment clause.
- Pre-existing IP (vendor's background IP) used in deliverable — vendor retains ownership, buyer gets license: 🟡 MEDIUM — acceptable only if license is broad, perpetual, and irrevocable.
- Deliverable incorporates open-source under copyleft license — may infect buyer's proprietary code: 🟠 HIGH.
- Third-party components used without disclosure or license: 🟠 HIGH.
- Deliverable incorporates vendor's proprietary framework — buyer cannot maintain without vendor: 🟠 HIGH.

---

## 3. Acceptance Testing

**Flag:**
- No formal acceptance testing (UAT/ATP) process: 🟠 HIGH.
- Automatic acceptance — if buyer doesn't reject within X days, product is "accepted": 🟠 HIGH. X should be ≥ 10 business days.
- Acceptance criteria defined by vendor: 🟠 HIGH — buyer must define acceptance criteria.
- No defect severity classification — P1 bugs treated same as cosmetic issues: 🟡 MEDIUM.
- Vendor can deliver a "substantially conforming" product and claim acceptance: 🟡 MEDIUM.

---

## 4. Warranty and Bug Fixing

**Flag:**
- Post-acceptance warranty period < 3 months: 🟠 HIGH (industry standard: 3–12 months).
- Warranty covers only "new" bugs — bugs present in delivered code but not noticed during UAT excluded: 🟠 HIGH.
- Bug fixes during warranty at hourly T&M rates: 🟠 HIGH — warranty period bug fixes should be at no charge.
- No warranty on third-party components: 🟡 MEDIUM.

---

## 5. Source Code and Escrow

**Flag:**
- Source code not delivered to buyer (only binary/compiled deliverable): 🔴 CRITICAL — buyer cannot maintain, audit, or transfer the software.
- Source code delivered only at end of project — not incrementally: 🟡 MEDIUM.
- No escrow for vendor-retained IP components: 🟠 HIGH if those components are business-critical.
- Development repository (Git) not handed over: 🟠 HIGH — history, branches, and documentation lost.
- Code quality standards not specified — no code review, no tests, no documentation obligation: 🟡 MEDIUM.

---

## 6. Subcontracting

**Flag:**
- Vendor can subcontract any/all work without buyer consent: 🟠 HIGH — quality and security risks.
- No background check requirement for subcontractor staff accessing buyer systems/data: 🟠 HIGH.
- IP assignment chain unclear — vendor's subcontractor retains IP, vendor licenses to buyer: 🟠 HIGH.

---

## 7. Milestones and Payment

**Flag:**
- Payment schedule not tied to deliverable milestones — time-based only: 🟡 MEDIUM.
- Large upfront payment (> 30%) before any deliverable: 🟡 MEDIUM — consider phased payment.
- No holdback for final acceptance: 🟡 MEDIUM. Push for 10–20% held until final UAT sign-off.
- Milestone acceptance criteria vague: 🟡 MEDIUM.
