# E-commerce Data Analysis Project

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Key Findings](#key-findings)
- [Recommendations](#recommendations)
- [Conclusion](#conclusion)

## Project Overview

This project analyzes an e-commerce dataset to understand key drivers of business performance, customer behavior, and customer experience.

The analysis focuses on identifying growth patterns, retention issues, and operational factors affecting user satisfaction.

---

## Tech Stack

- Python (Pandas, NumPy)
- SQL (SQLite)
- Data Visualization (Matplotlib)
- Jupyter Notebook

---

## Dataset

- Source: [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- Description:
  This dataset contains real e-commerce data from Olist, a Brazilian online marketplace.

- Main tables:
  - orders: order status and timestamps
  - order_items: product-level transaction data
  - customers: customer location and identifiers
  - sellers: seller information
  - products: product attributes and categories
  - order_payments: payment types and values
  - order_reviews: customer review scores and comments

- Time range:
  2016–2018

---

## Project Structure

```plaintext
daproject/
│
├── data/
│   └── olist.sqlite              # Raw dataset (SQLite)
│
├── notebooks/
│   ├── data_overview.ipynb       # Schema exploration
│   ├── eda.ipynb                 # Exploratory data analysis
│   ├── analysis.ipynb            # Business analysis
│   └── test.py                   # Testing scripts
│
├── report/
│   └── insight.md                # Final insights & recommendations
│
├── src/
│   ├── data_scope.py             # Data loading & filtering logic
│   └── metrics.py                # Metric calculations (GMV, AOV, etc.)
│
├── .gitignore
├── README.md
```
---

## Key Findings

- The platform relies heavily on new customers, with a very low repeat purchase rate (~3%).
- Late delivery significantly reduces customer satisfaction (average rating drops from ~4.3 to ~2.6).
- Approximately 17.5% of sellers contribute 80% of total GMV, indicating strong seller concentration.
- GMV growth is primarily driven by increasing order volume rather than higher spending per order.
- Product categories follow different revenue patterns, including both volume-driven and price-driven models.

---

## Recommendations

- Improve customer retention through loyalty programs and personalized recommendations.
- Optimize delivery performance to reduce delays and improve customer satisfaction.
- Reduce dependency on top sellers by supporting mid-tier sellers.
- Focus on sustainable growth by increasing repeat purchases and customer lifetime value.
- Invest in high-performing product categories and optimize product strategy.

---

## Conclusion

This project demonstrates how data analysis can uncover key business drivers and translate insights into actionable strategies for improving growth and customer experience.
