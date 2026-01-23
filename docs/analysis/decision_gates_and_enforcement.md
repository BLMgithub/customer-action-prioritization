# **Decision Gates and Enforcement**

**Doc Scope:** Define the conditions under which customer facing effort may vary under finite execution capacity.

**Related Notebook:** [`05_prioritization_analysis.ipynb`](../../notebooks/05_prioritization_analysis.ipynb)

## **Decision Gates**

### **Gate 1: Eligibility for Differentiation**

**Decision:** <ins>Can this customer receive non-standard treatment?</ins>

Criteria:
- Customer behavior must be clearly distinct and defensible
- Geographic context alone is insufficient justification

Outcome: 
- If criteria aren't met, customers are restricted to Standardized or Minimal handling. No differentiation beyond this is valid

---

### **Gate 2: Approved Behavioral Signals**

**Decision:** <ins>Which inputs may influence treatment decisions?</ins>

**Allowed signals:**
- **Seasonality** - purchasing pattern timing
- **Cancellation stability** - consistency of retention behavior

**Restrictions:**
- No model outputs, segments, or abstract scores
- Signals constrain effort application, not customer ranking

---

### **Gate 3: Treatment Band Assignment**

**Decision:** <ins>What execution effort levels are permitted?</ins>

**Available treatment bands:**
- **High-touch:** Manual, bespoke actions requiring concentrated effort
- **Standardized:** Repeatable actions applied broadly
- **Minimal/Automated:** Low-effort or system-driven actions

**Assignment rules:**
- Each customer occupies exactly one band
- Standardized is the default
- **Seasonality** - constrains timing within Standardized/Automated only
- **Cancellation stability** - permits Minimal/Automated only
- **No behavioral signal** <ins>authorizes High-touch assignment</ins>

## **Enforcement Rules**
- Most restrictive eligible band applies
- Zero High-touch assignments is valid
- No discretionary escalation permitted

## **Out of Scope**

This framework does not support:
- Customer ranking or scoring
- Model outputs as decision inputs
- Forced differentiation
