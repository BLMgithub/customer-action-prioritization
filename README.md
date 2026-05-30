# Customer Action Prioritization

## Overview

This project evaluates whether customer-facing effort should be differentiated based on observed behavioral patterns under finite execution capacity.

The analysis uses a decision gate prioritization diagnostic to test whether customer behavior demonstrates actionable differences that justify varying levels of execution effort. When justification is absent, the analysis enforces standardized or automated handling. This protects limited human capacity from misallocation against indefensible signals, rather than ranking customers or optimizing engagement strategies.

The pipeline surfaces only signals that can change execution effort and explicitly rules out those that cannot.

## Decision context

**Decision:**
Whether customer-facing behavior justifies any escalation to differentiated handling under current execution constraints.

**Mandate:**
- Prevent wasted human effort under finite capacity
- Treat misclassification cost as material
- Accept inaction as a valid and deliberate outcome

> Executive deliverable (decision narrative + recommendations): [`Executive Decision Summary (Website)`](https://bryan-melvida.super.site/data-analytics/customer-effort-prioritization-diagnostic)

## Deliverables
- Executive Summary (Website Format) 
- Decision framework and enforcement contract
- Prioritization diagnostic notebooks
- Decision ready customer behavior profile 
- Documented assumptions and exclusions

## How the analysis is structured

- `01_data_cleaning.ipynb`
   - Validate transactional integrity and structural consistency  
   - Correct issues that materially affect behavioral interpretation  
   - Establish a reliable analytical base  

- `02_feature_engineering.ipynb`
   - Translate transactions into customer-level behavioral signals  
   - Encode timing, persistence, and efficiency in an interpretable feature set  

- `03_dimensionality_reduction.ipynb`
   - Test variance-based transformations against the scaled base features  
   - Decide whether dimensionality reduction preserves behavioral structure  

- `04_clustering_analysis.ipynb`
   - Assess whether behavioral features support defensible segmentation under finite capacity  
   - Accept or constrain clusters based on clear behavioral separation  

- `05_prioritization_analysis.ipynb`
   - Map behavioral differences to execution relevant treatment constraints  
   - Block differentiation where signals do not justify action  

## Repository structure

```
├── data/
│   ├── raw/                                   # original source data
│   ├── cleaned/                               # validated and cleaned datasets
│   ├── preprocessed/                          # feature-engineered datasets
│   └── final/                                 # decision ready customer behavior profiles
├── docs/
│   ├── analysis/
│   │   └── decision_gates_and_enforcement.md  # source-of-truth decision framework
│   ├── data_handling/
│   │   └── data_handling_log.md               # preprocessing and data handling logs
│   ├── feature_engineering/
│   │   ├── feature_definitions.md             # feature definitions
│   │   └── feature_rationale.md               # feature design rationale
│   └── raw/
│       └── customer_raw_dictionary.md         # source data documentation
├── notebooks/
│   ├── 01_data_cleaning.ipynb                 # data validation and cleaning
│   ├── 02_feature_engineering.ipynb           # behavioral feature construction
│   ├── 03_dimensionality_reduction.ipynb      # structure viability testing
│   ├── 04_clustering_analysis.ipynb           # segmentation diagnostics
│   └── 05_prioritization_analysis.ipynb       # decision enforcement and outcome
└── src/                                       # shared plotting and assessment utilities
```

## Scope boundaries

This project intentionally does **not**:

- Rank or score customers
- Force segmentation where behavior does not support it
- Use model artifacts as decision inputs
- Optimize execution tactics or staffing plans
- Recommend engagement strategies absent defensible eligibility

Its purpose is to determine whether prioritization is justified at all, and to constrain execution effort accordingly.
