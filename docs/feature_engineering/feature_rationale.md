# Feature Definitions

**Doc Scope:** Behavioral and decision-oriented justification for engineered features, outlining the behavioral dimensions each feature encodes and how those distinctions support customer segmentation and action prioritization under operational constraints.

**Related Notebook:** [`02_feature_engineering.ipynb`](../../notebooks/02_feature_engineering.ipynb)

**Output dataset:** [`customer_features.parquet`](../../data/preprocessed/customer_features.parquet)

| Feature Name | Behavioral Dimension | What It Distinguishes | Why It Matters for Prioritization |
| --- | --- | --- | --- |
| cancellation_rate | Stability | Reliable vs Reversal-prone customers | High cancellation rates increase execution cost and reduce action effectiveness |
| days_since_last_purchase | Timing | Active vs Lapsed engagement | Supports timing-sensitive allocation of outreach and effort |
| total_transaction | Persistence | Sustained vs Episodic engagement | Indicates durability of customer relationship |
| avg_order_value | Efficiency | Low vs High yield interactions | Helps justify differentiated effort intensity |
| avg_days_between_purchases | Rhythm | Predictable vs Irregular buyers | Impacts planning and execution rhythm |
| n_unique_purchased_product | Complexity | Focused vs Diverse purchasing behavior | Signals operational handling complexity |
| product_repeat_rate | Loyalty vs Exploration | Repeat buyers vs Explorers | Informs standardization vs customization |
| is_seasonal | Temporal Concentration | Continuous vs Episodic customers | Prevents mis-timed actions outside active windows |
| is_uk_customer | Operational Context | Domestic vs International customers | Provides context without driving segmentation |