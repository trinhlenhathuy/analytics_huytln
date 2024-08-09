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






















git clone https://github.com/trinhlenhathuy/analytics_huytln.git 

cd analytics_huytln

python setup.py sdist bdist_wheel 

twine upload --config-file C:\Users\huytln\analytics_huytln\.pypirc dist/*
