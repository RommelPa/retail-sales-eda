# Retail Sales Intelligence: Exploratory Data Analysis for Business Decisions

## Overview

This project analyzes online retail transaction data to identify sales patterns, customer behavior, product performance, cancellation impact, and business opportunities.

The goal is not only to create visualizations, but to transform raw transactional data into useful business insights.

## Business Context

Retail companies need to understand their sales behavior before making decisions about pricing, inventory, marketing, customer retention, and international expansion.

Before building predictive models, it is necessary to understand the quality, structure, limitations, and business meaning of the available data.

## Dataset

This project uses the **Online Retail** dataset from the UCI Machine Learning Repository.

The dataset contains transactional data from a UK-based online retail company between December 2010 and December 2011.

Main variables include:

- `InvoiceNo`: transaction identifier.
- `StockCode`: product identifier.
- `Description`: product description.
- `Quantity`: number of items purchased.
- `InvoiceDate`: transaction date and time.
- `UnitPrice`: product unit price.
- `CustomerID`: customer identifier.
- `Country`: customer country.

Invoices starting with `C` represent cancellations.

Dataset source: UCI Machine Learning Repository.

## Objectives

- Audit data quality.
- Clean and prepare transactional data.
- Analyze revenue trends.
- Identify top products and countries.
- Measure customer concentration.
- Evaluate cancellation impact.
- Detect outliers and unusual transactions.
- Generate business recommendations.

## Project Structure

```text
retail-sales-eda/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_exploratory_analysis.ipynb
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── feature_engineering.py
│   └── visualization.py
├── reports/
│   ├── executive_summary_en.md
│   ├── resumen_ejecutivo_es.md
│   └── figures/
├── README.md
├── requirements.txt
└── .gitignore
```

## Analytical Questions

This project aims to answer the following questions:

1. How does revenue evolve over time?
2. Which products generate the highest revenue?
3. Which countries contribute the most to sales?
4. How concentrated is revenue among customers?
5. What is the impact of cancellations?
6. What is the average order value?
7. Are there outliers or suspicious transactions?
8. What business actions could be recommended?

## Tools

- Python
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- Jupyter Notebook

## Status

Project in progress.