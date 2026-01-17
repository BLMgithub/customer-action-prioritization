## Customer Raw Dictionary

**Doc scope:** Source notes and Field dictionary for reference for [`customer_raw.parquet`](../../data/raw/customer_raw.parquet) or [`Online Retail.xlsx`](../../data/raw/Online%20Retail.xlsx)

Source: UCI Machine Learning Repository  
Description: UK based online retail transactional data  
Coverage: 01/12/2010 – 09/12/2011

| Field Name | Data  Type | Description |
| --- | --- | --- |
| InvoiceNo | object | 6-digit unique code assigned for each transaction. If this code starts with letter 'c', it indicates a cancellation |
| StockCode | object | 5-digit unique code assigned to each distinct product |
| Description | object | Description for each product |
| Quantity | int | Quantities of each product (item) per transaction |
| InvoiceDate | datetime | Day and time when each transaction was generated |
| UnitPrice | float | Product price per unit in sterling (GBP) |
| CustomerID | float | 5-digit unique code assigned to each customer |
| Country | object | The Country where the customer resides |