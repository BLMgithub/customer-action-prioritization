# Data Handling Log
## Data Quality & Field Handling

**Doc Scope:** Field-level documentation of data quality issues, corrections, and data handling decisions applied during preprocessing.

**Related script:** [`01_data_cleaning.ipynb`](../../notebooks/01_data_cleaning.ipynb)

**Output dataset:** [`customer_cleaned.parquet`](../../data/cleaned/customer_cleaned.parquet)

| Field Name | Issue Identified | Action Taken | Notes |
| --- | --- | --- | --- |
| CustomerID | Missing values | Remove records with missing values | Applied to maintain consistent customer-level identifiers |
| StockCode | Non-standard 5-digit format | Remove non-conforming records | Based on data dictionary specification |
| StockCode | Multiple descriptions per code | Remove inconsistent records | Enforced one-to-one mapping |
| Description | Multiple stock codes per description | Remove inconsistent records | Applied where ambiguity exists |
| Quantity | Extreme value ranges | Retain records | Linked to cancelled transactions |
| UnitPrice | Extreme value ranges | Retain records | Linked to cancelled transactions |
| Invoice-level Record | Duplicate records | Remove duplicate rows | First occurrence retained |