# Severity Grading — Context-Based Adjustments

Default severity for each finding is set in the reference checklists. Use this table to **adjust** based on buyer context established in Step 0.

---

## Severity Levels

| Level | Symbol | Meaning |
|---|---|---|
| Critical | 🔴 | Block signing. Must be resolved before proceeding. |
| High | 🟠 | Strong recommendation to negotiate before signing. Significant risk if left as-is. |
| Medium | 🟡 | Worth raising in negotiation; tolerable if vendor won't move. |
| Informational | ⓘ | Note for awareness; no action required. |

---

## Adjustment Rules by Context

### Production-critical / business-critical systems (revenue/operations stops if vendor fails)

| Default | → Adjusted | Trigger |
|---|---|---|
| 🟡 No 24/7 P1 support | → 🟠 | Any production-critical |
| 🟠 SLA credits < 1 month fee | → 🔴 | Business-critical |
| 🟡 NBD hardware maintenance | → 🟠 | Business-critical hardware |
| 🟠 Force majeure covers cloud infra failures | → 🔴 | Business-critical |
| 🟡 No DR plan documented | → 🟠 | Business-critical |
| 🟡 Vendor can suspend for non-payment (no cure) | → 🟠 | Business-critical |
| 🟠 No termination-for-convenience | → 🔴 | Business-critical with long term (>2yr) |

### Personal data / GDPR scope

| Default | → Adjusted | Trigger |
|---|---|---|
| 🟡 No DPA | → 🔴 | Any personal data processed |
| 🟡 US sub-processors without DPF/SCCs | → 🔴 | Personal data |
| 🟡 No breach notification in contract | → 🔴 | Personal data |
| 🟡 Retention period unspecified | → 🟠 | Personal data |
| 🟡 AI training on data | → 🔴 | Personal data, regulated data |

### Regulated data (financial, health, biometric, children's data)

All GDPR findings upgrade one level. Additionally:
- Absence of DORA compliance (financial sector): 🔴 CRITICAL.
- Absence of NIS2 consideration (critical infrastructure): 🔴 CRITICAL.
- Non-EU data storage for regulated data: 🔴 CRITICAL.

### Non-critical / PoC / pilot

| Default | → Adjusted | Trigger |
|---|---|---|
| 🟠 Low SLA uptime (99%) | → 🟡 | PoC/pilot |
| 🔴 No DR plan | → 🟠 | PoC (but flag for production phase) |
| 🟠 Credit sole remedy | → 🟡 | PoC |

### US vendor (non-EU governing law)

- Non-EU jurisdiction: 🟠 in all cases (upgrade if combined with other risks).
- Arbitration in US with loser-pays: 🟠.
- CLOUD Act exposure (US vendor can be compelled to provide EU data to US authorities): 🟠 for any personal data.

---

## Absence Severity Defaults

When a critical clause is entirely absent (not just poorly worded):

| Missing clause | Default severity |
|---|---|
| SLA / uptime commitment | 🔴 |
| Support SLA | 🟠 |
| Termination for convenience | 🟠 |
| Data return obligation | 🟠 |
| DPA (if personal data) | 🔴 |
| IP ownership (custom dev) | 🔴 |
| Limitation of liability | 🟠 |
| Exit / transition assistance | 🟠 |
| Source code delivery (custom dev) | 🔴 |
| Security certification requirement | 🟠 |
