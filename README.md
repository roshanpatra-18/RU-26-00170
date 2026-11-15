# E-Commerce Sales Analyzer

Python 3 console application built with Pandas and Matplotlib for Rungta International Skills University to analyze, clean, and visualize e-commerce order data[cite: 1, 2].

## Overview
The **E-Commerce Sales Analyzer** is a Python 3 console application developed for Rungta International Skills University (RISU)[cite: 1, 2]. It reads order data from a CSV file, cleans corrupted or invalid records using Pandas, computes key sales metrics and aggregations, and visualizes category-wise revenue distribution using Matplotlib[cite: 1].

---

## Features
* **Data Cleaning & Validation:** Automatically detects and skips invalid data rows (such as negative prices or non-numeric quantities)[cite: 1].
* **Automated Calculations:** Computes individual row revenue ($\text{Quantity} \times \text{Price}$), total store revenue, total orders, and total units sold[cite: 1].
* **Interactive Console Menu:** Provides a simple menu to toggle between summary performance reports and category-wise analysis[cite: 1].
* **Data Visualizations:** Generates side-by-side Matplotlib charts (Bar chart and Pie chart) displaying category-wise revenue and percentage shares[cite: 1].

---

## Tech Stack
* **Language:** Python 3[cite: 1]
* **Libraries:** `pandas`, `matplotlib`[cite: 1]

---

## How to Run
1. Ensure Python 3 and the required libraries are installed:
   ```bash
   pip install pandas matplotlib