# Executive Summary — Retail Sales Intelligence EDA

## 1. Objective

This project analyzes online retail transaction data to identify revenue patterns, customer behavior, product performance, cancellation impact, and business opportunities.

The objective is to understand the business before building predictive models, dashboards, or customer segmentation systems.

## 2. Dataset Scope

After removing exact duplicate rows, the cleaned dataset contains:

| Dataset | Rows | Purpose |
|---|---:|---|
| Clean data | 536,641 | Full enriched dataset with business flags |
| Valid sales | 524,878 | Main dataset for revenue, products, countries, and time trends |
| Customer sales | 392,692 | Subset for customer-level analysis |

Valid sales revenue reached **10.64M**.

Customer-identified revenue reached **8.89M**, which means **1.75M** in valid revenue cannot be linked to a known customer.

This represents **16.49%** of valid sales revenue.

## 3. Key Findings

### 3.1 Data quality issues are business-relevant

The raw dataset included duplicate rows, missing customer identifiers, cancellations, non-positive quantities, and non-positive unit prices.

These records should not be removed blindly. Some of them represent real business events, especially cancellations and operational adjustments.

### 3.2 Revenue is highly concentrated in the United Kingdom

The United Kingdom represents approximately **85%** of valid sales revenue.

This shows strong dependence on the domestic market. It also means that international performance should be analyzed separately, because smaller markets can be hidden by the dominance of the United Kingdom.

### 3.3 December 2011 is a partial month

Revenue increased strongly between September and November 2011.

However, December 2011 should not be compared directly with previous months because the dataset only contains transactions up to December 9.

### 3.4 Customer revenue is meaningfully concentrated

The top 10 identified customers generate **17.30%** of customer-identified revenue.

The top 100 identified customers generate **40.61%** of customer-identified revenue and approximately **33.91%** of total valid sales revenue.

This suggests that a relatively small group of customers has a meaningful impact on business performance.

### 3.5 Cancellations have a material revenue impact

Cancellations represent a negative revenue impact of approximately **894K**, equivalent to **8.40%** of valid sales revenue.

This should be investigated as a business and operational issue, not discarded as simple noise.

### 3.6 Product ranking requires business interpretation

Some high-revenue records are not regular product items. Examples include postage, manual adjustments, or operational codes.

For this reason, product performance was analyzed both with and without special operational codes.

The item `PAPER CRAFT , LITTLE BIRDIE` shows unusually high revenue from a very small number of invoices, so it should be treated as a potential outlier requiring business validation.

### 3.7 Order values are highly skewed

The average order value is **533.17**, while the median order value is **303.30**.

This indicates that a small number of large orders can distort average-based interpretations. Median and percentile-based metrics are more reliable for understanding typical order behavior.

## 4. Business Recommendations

1. Monitor high-value customers separately because they represent a significant share of customer-identified revenue.
2. Analyze international markets excluding the United Kingdom to identify growth opportunities hidden by the dominant domestic market.
3. Investigate cancellation patterns by product, country, and customer to identify operational friction.
4. Separate operational codes from product rankings to avoid confusing charges or adjustments with merchandise performance.
5. Use median and percentile-based metrics for order value analysis instead of relying only on averages.
6. Treat missing customer identifiers as a data quality limitation before performing customer segmentation or retention analysis.

## 5. Limitations

- The dataset covers transactions from December 2010 to December 2011 only.
- December 2011 is incomplete and should not be compared directly with full months.
- Around 16.49% of valid sales revenue has no associated customer identifier.
- The dataset does not include product cost, profit margin, marketing spend, inventory levels, or customer demographics.
- Some high-revenue records may represent operational adjustments rather than regular product sales.

## 6. Next Steps

- Create a customer segmentation project using the customer-identified subset.
- Build a sales dashboard for executive reporting.
- Analyze cancellation drivers in more detail.
- Apply forecasting techniques to monthly revenue or sales volume.