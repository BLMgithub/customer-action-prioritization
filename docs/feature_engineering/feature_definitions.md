# Feature Definitions

**Doc Scope:** Field-level specification of engineered customer features, including precise definitions, calculation grain, and raw data dependencies. This document serves as the authoritative contract for feature construction and reproducibility following feature engineering.

**Related script:** [`02_feature_engineering.ipynb`](../../notebooks/02_feature_engineering.ipynb)

**Output dataset:** [`customer_features.parquet`](../../data/preprocessed/customer_features.parquet)

>All features are computed at the customer level for customers with more than one observed transaction. One-time buyers are excluded due to insufficient behavioral history

| Feature Name | Definition | Calculation Level | Key Inputs | Notes |
| --- | --- | --- | --- | --- |
| cancellation_rate | Proportion of cancelled transactions relative to total transactions | Customer | InvoiceNo, CustomerID | — |
| days_since_last_purchase | Number of days between last transaction date and reference date | Customer | InvoiceDate, CustomerID | — |
| total_transaction | Count of transactions | Customer | InvoiceNo, CustomerID | Includes cancelled transactions |
| avg_order_value | Mean monetary value per transaction | Customer | Quantity, UnitPrice, CustomerID | — |
| avg_days_between_purchases | Mean interval between successive transactions | Customer | InvoiceDate, CustomerID | — |
| n_unique_purchased_product | Count of distinct products purchased | Customer | StockCode, CustomerID | — |
| product_repeat_rate | Ratio of repeat product purchases to total product purchases | Customer | StockCode, CustomerID | — |
| is_seasonal | Indicator for customers with spend concentrated in limited time windows | Customer | InvoiceDate, Quantity, UnitPrice, CustomerID | Threshold defined in notebook |
| is_uk_customer | Indicator for UK-based customers | Customer | Country, CustomerID | Contextual feature only |