Analytics by Huytln - Unlock powerful, customizable, and insightful visualizations with just one line of code.
==============================================================================================================

.. image:: https://img.shields.io/pypi/pyversions/analytics-huytln
   :alt: Python Versions

.. image:: https://img.shields.io/pypi/l/analytics-huytln
   :alt: License

.. image:: https://img.shields.io/pypi/v/analytics-huytln
   :alt: PyPI Version

`analytics-huytln` is a Python library designed to assist in data analysis through various charts and data visualizations. 
The goal of this library is to make it easier for analysts and data scientists to explore, analyze, and present their data.

Contents Overview
-----------------
What's new in the version
---------------------

.. image:: https://img.shields.io/pypi/v/analytics-huytln
   :alt: PyPI Version

- Deploy "Trend Analysis Chart & Forecast" by linear regression
   + Normal forecast
   + Seasonality

.. image:: https://img.shields.io/badge/version-0.2.7-blue
   :alt: Version 0.2.7
   :target: https://pypi.org/project/analytics-huytln/

-  Allow the plotting function to be applied to a DataFrame with more columns than the required number of columns.
-  Allow to export raw data from chart
-  Adjust heatmap by timing function -> plot_heatmap_by_2_dimensions function to allow flexible input of two dimensions.

.. contents::
   :depth: 3
   :local:

Features
--------

- **Easy Data Analysis**: Provides powerful tools for data analysis with convenient functions and methods.
- **Chart Creation**: Supports various common charts for data visualization.
  
  - Pareto chart
  - Heatmap by 2 dimensions
  - Trend Analysis & Forecast

- **High Compatibility**: Works well with popular data formats such as CSV, Excel, JSON.
- **User-Friendly**: Offers user-friendly functions that are easy to use and integrate into existing projects.

Installation
------------

Install `analytics-huytln` via pip:

.. code-block:: bash

    pip install --upgrade analytics-huytln

Modules Usage
-------------

- `plot pareto chart`_

  - `Parameters pareto`_
  - `Usage pareto`_
  - `Output pareto`_
  - `Analyse pareto`_

- `heatmap by 2 dimensions`_

  - `Parameters heatmap`_
  - `Usage heatmap`_
  - `Output heatmap`_
  - `Analyse heatmap`_

- `trend analysis and forecast`_

  - `Parameters Trend analysis`_
  - `Usage Trend analysis`_
  - `Output Trend analysis`_
  - `Analyse Trend analysis`_

- `Seasonality Trend Analysis and Forecast`_

  - `Parameters seasonality trend analysis`_
  - `Usage seasonality trend analysis`_
  - `Output seasonality trend analysis`_
  - `Analyse seasonality trend analysis`_

- `incoming insightful charts`_

---------------------------------------------------------------------------------------------------------------------------

plot pareto chart
=================

.. _plot_pareto_chart:

The `plot_pareto_chart` function creates a Pareto chart from Excel data.

.. _Parameters_pareto:

Parameters pareto
-----------------

- **df** (*pandas.DataFrame*): DataFrame containing the data with dim_name (category) and metric (value) columns.
- **dim_name** (*str*): Name of the column representing the category (e.g., SKU).
- **metric** (*str*): Name of the column containing the values to analyze (e.g., Sales).
- **save_to_excel** (*binary*): (optional) 1 to export data, default by 0

.. _Usage_pareto:

Usage pareto
------------

Here's how to use the `plot_pareto_chart` function:

.. code-block:: python

    import pandas as pd
    from pareto_chart_lib.pareto import plot_pareto_chart

    # Read data from Excel file
    df = pd.read_excel('data_pareto.xlsx')

    # Create a Pareto chart
    plot_pareto_chart(df, 'SKU', 'Sales')

.. _Output_pareto:

Output pareto
-------------

.. image:: https://github.com/user-attachments/assets/f2147e62-dc28-486c-8176-b5d763811c47
   :width: 830px
   :alt: Pareto Chart Output

.. _Analyse_pareto:

Analyse pareto
--------------

**Chart Components**:

- **Histogram (Blue Bars)**: Represents the number of sales for each SKU. The SKUs are sorted in descending order of sales, with the most sold SKU on the left.
- **Cumulative Percentage Curve (Orange Line)**: Represents the cumulative percentage of total sales as you move from left to right across the SKUs. The percentage curve helps identify the SKUs that contribute to a significant portion of the total sales.
- **Horizontal Lines**: Dotted lines at 80% and 95% cumulative sales percentage mark important thresholds.
- **Annotations**: The chart marks specific SKUs (SKU 10 and SKU 32) that correspond to the 80% and 95% cumulative sales levels.

**Table**:

- **Level**: Indicates the cumulative percentage levels (80% and 95%).
- **Total Sales**: The total number of sales up to the specified cumulative percentage.
- **Total SKUs to X%**: The number of SKUs contributing to the specified cumulative percentage.
- **Percent of SKU**: The percentage of SKUs contributing to the specified cumulative percentage of sales.

**Analysis**:

- **80% of Sales**:
    - SKU 10 is the last SKU contributing to 80% of total sales.
    - Only 7 SKUs (5.00% of the total SKUs) are responsible for generating 80% of the sales. This indicates that a small number of SKUs are driving the majority of the sales, which is consistent with the Pareto principle (80/20 rule).

- **95% of Sales**:
    - SKU 32 is the last SKU contributing to 95% of total sales.
    - 30 SKUs (21.43% of the total SKUs) contribute to 95% of the sales.

**Conclusion**:

This Pareto chart visually emphasizes that a small fraction of SKUs contributes to a large fraction of total sales. This insight can help prioritize inventory management, marketing efforts, and sales strategies focusing on the top-performing SKUs.

heatmap by 2 dimensions
=======================

.. _heatmap_by_2_dimensions:

The `plot_heatmap_by_2_dimensions` function creates a visual representation of sales data, illustrating the relationship between two dimensions (e.g., time and SKU) and highlighting significant sales periods. This function allows for flexible input of two dimensions to explore and emphasize their correlation effectively.

.. _Parameters_heatmap:

Parameters heatmap
------------------

- **df** (*pandas.DataFrame*): DataFrame containing the data with dim_name (category) and metric (value) columns.
- **dim_name_x** (*str*): Name of the horizontal column representing the category 1 (e.g., Timing, percent of discount).
- **dim_name_y** (*str*): Name of the vertical column representing the category 2 (e.g., SKU).
- **metric** (*str*): Name of the column containing the values to analyze (e.g., Sales).
- **highlight** (*int*): The number of top points to be highlighted.
- **save_to_excel** (*binary*): (optional) 1 to export data, default by 0

.. _Usage_heatmap:

Usage heatmap
-------------

Here's how to use the `plot_heatmap_by_2_dimensions` function:

.. code-block:: python

    import pandas as pd
    from heatmap_by_2_dimensions.heatmap_by_2_dimensions import plot_heatmap_by_2_dimensions

    # Read data from Excel file
    df = pd.read_excel('data_order_by_time.xlsx')

    # Create a heatmap by timing and SKU with the top 10 highest sales points highlighted
    plot_heatmap_by_2_dimensions(df, 'timing', 'SKU', 'Sales', 10)

.. _Output_heatmap:

Output heatmap
--------------

.. image:: https://github.com/user-attachments/assets/208cf8bd-70ff-4734-9a56-d3d96679d1f2
   :width: 704px
   :alt: Heatmap Output

.. _Analyse_heatmap:

Analyse heatmap
---------------

**Chart Components**:

- **X-axis (Timing)**: The timing is represented as a concatenation of the day of the week and hour.
- **Y-axis (SKU)**: Represents different SKUs, with each row dedicated to a specific SKU. 
- **Scatter Plot (Dots)**:
    - **Data Points**: Each dot represents a sale of a specific SKU at a particular time.
    - **Color and Size**: The dots vary in size and color, representing the quantity of items sold. Larger dots indicate higher quantities or larger sales amounts.
    - **Vertical Lines (Red)**: These lines represent the times with the highest total sales across all SKUs.

**Table**:

- **Time Periods**: The chart could be segmented by specific time periods (days or hours) to analyze how sales performance fluctuates during these periods.
- **Top SKUs**: The distribution of sales across different SKUs can help identify top-performing SKUs at various times, similar to how a Pareto chart highlights top contributors.

**Analysis**:

- **Sales Concentration**:
    - There are visible clusters of sales activity at certain times, indicating peak periods where specific SKUs are more popular.
    - The distribution suggests that certain SKUs have consistent sales across different times, while others may peak during specific hours or days.

- **Timing Patterns**:
    - The timing axis shows a dense clustering of sales at specific periods, which might correlate with customer behavior, promotional activities, or operational factors.
    - The overlap of timing labels suggests that further aggregation or a different representation (e.g., hourly or daily aggregates) could provide clearer insights.

- **Impact of Vertical Lines**:
    - The red vertical lines likely mark significant time thresholds, which could be used to analyze how sales change before and after these periods.
    - These lines might highlight the impact of certain events, such as promotions, holidays, or restocking, on sales patterns.

**Conclusion**:

This scatter plot provides a comprehensive view of sales distribution across different SKUs and times. The clustering of dots and the variations in size and color reveal key insights into sales performance, indicating peak periods and top-performing SKUs. The vertical lines and timing axis add another layer of insight into sales trends and periods of interest.

trend analysis and forecast
===========================

.. _trend_analysis_and_forecast:

The `plot_trend_analysis_normal` function performs trend analysis and forecasts future values using linear regression on time series data.

.. _Parameters_trend_analysis:

Parameters Trend analysis
-------------------------

- **df** (*pandas.DataFrame*): DataFrame containing the time series data with columns for time dimension and metric values.
- **time_dimension** (*Date*): Name of the column representing the time dimension (e.g., Date).
- **metric** (*str*): Name of the column containing the values to analyze (e.g., Sales).
- **forecast_periods** (*int*): (optional) Number of periods to forecast into the future (default is 12).

.. _Usage_trend_analysis:

Usage Trend analysis
--------------------

Here's how to use the `plot_trend_analysis_normal` function:

.. code-block:: python

   import pandas as pd
   from linear_forecast_lib.linear_forecast import plot_trend_analysis_normal

    # Read data from Excel file
   df = pd.read_excel('data_trend.xlsx')
   
   # Create a trend analysis chart
   plot_trend_analysis_normal(df, 'Date', 'Sales', 12)

.. _Output_trend_analysis:

Output Trend analysis
---------------------
- Trend Line: Displays the observed values and the forecasted values along with the linear regression line.

- Analysis Table: Provides key metrics and comments on the regression analysis.

.. _Analyse_trend_analysis:

Analyse Trend analysis
----------------------
**Chart Components**:

- **Trend Line (Observed and Forecast)**: Shows the actual values and the forecasted values, with the forecasted values indicated by a dashed line.
- **Regression Equation**: Displays the linear regression equation on the chart.
- **Analysis Table**: Includes metrics such as Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), p-value, Slope, R-squared, Mean Value, and Trend.

**Analysis Details**:

- **Mean Absolute Error (MAE)**: Indicates the average deviation of predictions from actual values.
- **Mean Absolute Percentage Error (MAPE)**: Shows the average percentage error of predictions.
- **p-value**: Tests the significance of the regression model.
- **Slope**: Represents the rate of change in the metric over time.
- **R-squared**: Measures the goodness of fit for the regression model.
- **Mean Valued**: Average value of the metric over the time period.
- **Trend**: Indicates whether the trend is positive or negative.

**Conclusions**:

- This trend analysis chart helps visualize the overall trend in the data and provides a forecast for future values. The analysis table gives a detailed breakdown of the regression metrics and their significance, which can be used to understand the performance and reliability of the forecast.

Seasonality Trend Analysis and Forecast
=======================================

.. _seasonality_trend_analysis_and_forecast:

The plot_trend_analysis_seasonality function performs trend analysis and forecasts future values using linear regression on time series data, incorporating seasonal patterns such as daily, weekly, monthly, or quarterly.

.. _Parameters_seasonality_trend_analysis:

Parameters Seasonality Trend Analysis
-------------------------

- **df** (*pandas.DataFrame*): DataFrame containing the time series data with columns for time dimension and metric values.
- **time_dimension** (*Date*): Name of the column representing the time dimension (e.g., Date).
- **metric** (*str*): Name of the column containing the values to analyze (e.g., Sales).
- **forecast_periods** (*int*): (optional) Number of periods to forecast into the future (default is 12).
- **seasonality** (*char*): (optional) Specifies the type of seasonality to consider. 
   - Possible values are 'D' for daily, 'W' for weekly, 'M' for monthly, and 'Q' for quarterly. Default is 'M'.

.. _Usage_seasonality_trend_analysis:

Usage Seasonality Trend Analysis
--------------------------------

Here's how to use the plot_trend_analysis_seasonality function:

.. code-block:: python

   import pandas as pd
   from linear_forecast_lib.linear_forecast import plot_trend_analysis_seasonality

    # Read data from Excel file
   df = pd.read_excel('data_trend.xlsx')
   
   # Create a trend analysis chart
   plot_trend_analysis_seasonality(df, 'Date', 'Sales', 12, 'M')

.. _Output_seasonality_trend_analysis:

Output Seasonality Trend Analysis
---------------------------------
.. image:: https://github.com/trinhlenhathuy/analytics_huytln/blob/main/images/trend_analysis_seasonality.png
   :width: 830px
   :alt: Pareto Chart Output

- Trend Line: Displays the observed values and the forecasted values along with the linear regression line.

- Analysis Table: Provides key metrics and comments on the regression analysis.

.. _Analyse_seasonality_trend_analysis:

Analyse Seasonality Trend Analysis
----------------------------------
**Chart Components**:

- **Trend Line (Observed and Forecast)**: Shows the actual values and the forecasted values, with the forecasted values indicated by a dashed line.
- **Seasonality Feature**: Displays the influence of seasonal patterns on the trend.
- **Regression Equation**: Displays the linear regression equation on the chart.
- **Analysis Table**: Includes metrics such as Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), p-value, Slope, R-squared, Mean Value, and Trend.

**Analysis Details**:

- **Mean Absolute Error (MAE)**: Indicates the average deviation of predictions from actual values.
- **Mean Absolute Percentage Error (MAPE)**: Shows the average percentage error of predictions.
- **p-value**: Tests the significance of the regression model.
- **Slope**: Represents the rate of change in the metric over time.
- **R-squared**: Measures the goodness of fit for the regression model.
- **Mean Valued**: Average value of the metric over the time period.
- **Trend**: Indicates whether the trend is positive or negative.

**Conclusions**:

- This seasonality trend analysis chart helps visualize the overall trend and seasonal patterns in the data. It provides a forecast for future values, considering both the trend and seasonality. The analysis table gives a detailed breakdown of the regression metrics and their significance, which can be used to understand the performance and reliability of the forecast.


incoming insightful charts
==========================

.. _incoming_insightful_charts:

- Correlation Heatmap
- Customer Segmentation
- Revenue Growth Tracker
- Sales Funnel Analysis
- Operational Efficiency Heatmap
- Candlestick Chart
- Sankey Multiple Levels

Let me know if you need further analysis or any specific insights!
==================================================================

.. code-block:: bash

    git clone https://github.com/trinhlenhathuy/analytics_huytln.git

    cd analytics_huytln

    python setup.py sdist bdist_wheel

    twine upload --config-file .pypirc dist/*

