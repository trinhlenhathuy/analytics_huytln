# Analytics by Huytln

![Python Versions](https://img.shields.io/pypi/pyversions/analytics-huytln)
![License](https://img.shields.io/pypi/l/analytics-huytln)
![PyPI Version](https://img.shields.io/pypi/v/analytics-huytln)

`analytics-huytln` is a Python library designed to assist in data analysis through various charts and data visualizations. The goal of this library is to make it easier for analysts and data scientists to explore, analyze, and present their data.

## Contents Overview

- [Features](#features)
- [Modules Usage](#modules-usage)
  - [plot_pareto_chart](#plot_pareto_chart)
    - [Parameters](#parameters)
    - [Usage](#usage)
    - [Output](#output)
    - [Analyse](#pareto_analyse)
    
## Features

- **Easy Data Analysis**: Provides powerful tools for data analysis with convenient functions and methods.
- **Chart Creation**: Supports various common charts for data visualization.
- **High Compatibility**: Works well with popular data formats such as CSV, Excel, JSON.
- **User-Friendly**: Offers a user-friendly API that is easy to integrate into existing projects.

## Installation

Install `analytics-huytln` via pip: 
```bash
pip install analytics-huytln
```

## Modules Usage

### plot_pareto_chart

The plot_pareto_chart function creates a Pareto chart from Excel data.

#### Parameters

- **df** (`pandas.DataFrame`): DataFrame containing the data with dim_name (category) and metric (value) columns.
- **dim_name** (`str`): Name of the column representing the category (e.g., SKU).
- **metric** (`str`): Name of the column containing the values to analyze (e.g., Sales).

#### Usage

Here's how to use the plot_pareto_chart function:

```python
import pandas as pd
from analytics_huytln import plot_pareto_chart

# Read data from Excel file
df = pd.read_excel(r'C:\Users\huytln\Desktop\Linkedln post pdf\data_pareto.xlsx')

# Create a Pareto chart
plot_pareto_chart(df, 'SKU', 'Sales')
```
#### Output
<img width="830" alt="image" src="https://github.com/user-attachments/assets/f2147e62-dc28-486c-8176-b5d763811c47">

#### Analyse
Chart Components:
- Histogram (Blue Bars): Represents the number of sales for each SKU.
The SKUs are sorted in descending order of sales, with the most sold SKU on the left.
- Cumulative Percentage Curve (Orange Line): Represents the cumulative percentage of total sales as you move from left to right across the SKUs.
- The percentage curve helps identify the SKUs that contribute to a significant portion of the total sales.
- Horizontal Lines: Dotted lines at 80% and 95% cumulative sales percentage mark important thresholds.
- Annotations: The chart marks specific SKUs (SKU 10 and SKU 32) that correspond to the 80% and 95% cumulative sales levels.

Table:
- Level: Indicates the cumulative percentage levels (80% and 95%).
- Total Sales: The total number of sales up to the specified cumulative percentage.
- Total SKUs to X%: The number of SKUs contributing to the specified cumulative percentage.
- Percent of SKU: The percentage of SKUs contributing to the specified cumulative percentage of sales.

Analysis:
- 80% of Sales:
    + SKU 10 is the last SKU contributing to 80% of total sales.
    + Only 7 SKUs (5.00% of the total SKUs) are responsible for generating 80% of the sales. This indicates that a small number of SKUs are driving the majority of the sales, which is consistent with the Pareto principle (80/20 rule).
- 95% of Sales:
    + SKU 32 is the last SKU contributing to 95% of total sales.
  + 30 SKUs (21.43% of the total SKUs) contribute to 95% of the sales.
 
Conclusion:
This Pareto chart visually emphasizes that a small fraction of SKUs contributes to a large fraction of total sales. This insight can help prioritize inventory management, marketing efforts, and sales strategies focusing on the top-performing SKUs.

Let me know if you need further analysis or any specific insights!





















git clone https://github.com/trinhlenhathuy/analytics_huytln.git 

cd analytics_huytln

python setup.py sdist bdist_wheel 

twine upload --config-file C:\Users\huytln\analytics_huytln\.pypirc dist/*
