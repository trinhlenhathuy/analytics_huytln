import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
import statsmodels.api as sm
from sklearn.preprocessing import OneHotEncoder

def plot_trend_analysis_normal(df, time_dimension, metric, forecast_periods=12):
    # Bước 1: Chuẩn bị dữ liệu để dự đoán
    df['Date_numeric'] = np.arange(len(df))

    # Tạo mô hình hồi quy tuyến tính
    model = LinearRegression()
    X = df[['Date_numeric']]
    y = df[metric]
    model.fit(X, y)
    y_pred = model.predict(X)

    # Tính các chỉ số hồi quy
    intercept = model.intercept_
    slope = model.coef_[0]
    r_squared = model.score(X, y)
    mae = mean_absolute_error(y, y_pred)
    mape = mean_absolute_percentage_error(y, y_pred)

    # Thêm hệ số chặn vào mô hình để tính p-value
    X_with_const = sm.add_constant(X)
    model_sm = sm.OLS(y, X_with_const)
    results = model_sm.fit()
    p_value = results.pvalues['Date_numeric']

    # Phân tích dựa vào hồi quy
    mean_value = df[metric].mean()
    trend_analysis = "Positive" if slope > 0 else "Negative"

    # Tạo bảng phân tích với cột chú thích thứ 3
    analysis_data = {
        'Metric': ['Mean Absolute Error', 'Mean Absolute Percentage Error', 'p_value', 'Slope', 'R-squared', 'Mean Value', 'Trend'],
        'Value': [f"{mae:.2f}", f"{mape*100:.2f}%", f"{p_value:.5f}", f"{slope:.2f}", f"{r_squared:.2f}", f"{mean_value:.2f}", trend_analysis],
        'Comment': [
            f'Predictions deviate by {mae:.2f} units from actual values on average',
            f'Prediction errors average {mape*100:.2f}% of the actual values',
            f'The result is {"Very significant" if p_value <= 0.001 else "Strongly significant" if p_value <= 0.01 else "Significant" if p_value <= 0.05 else "Weakly significant" if p_value <= 0.1 else "Not significant"} in predicted',
            f'The slope of {slope:.2f} establishes an {"increasing" if slope > 0 else "decreasing"} trend, \n with the value in the y column {"increasing" if slope > 0 else "decreasing"} by {abs(slope):.2f} units each month',
            f'The r-squared is {r_squared:.2f} and is evaluated as {"excellence" if r_squared > 0.9 else "very good" if r_squared > 0.7 else "good" if r_squared > 0.4 else "average" if r_squared > 0.2 else "bad"} correlation',
            'Average value over time period',
            f'Indicates {trend_analysis} trend'
        ]
    }
    analysis_df = pd.DataFrame(analysis_data)

    # Tạo dự đoán cho tương lai
    future_dates = pd.date_range(start=df[time_dimension].iloc[-1] + pd.DateOffset(months=1), periods=forecast_periods, freq='M')
    future_dates_numeric = np.arange(len(df), len(df) + len(future_dates))
    future_values = model.predict(future_dates_numeric.reshape(-1, 1))

    # Tạo DataFrame cho dữ liệu dự đoán
    df_future = pd.DataFrame({time_dimension: future_dates, metric: future_values})

    # Kết hợp dữ liệu gốc và dữ liệu dự đoán
    df_combined = pd.concat([df, df_future])

    # Bước 3: Vẽ biểu đồ xu hướng với dự đoán tương lai và bảng phân tích
    plt.figure(figsize=(12, 8))

    # Vẽ biểu đồ xu hướng
    plt.subplot(2, 1, 1)
    sns.lineplot(x=time_dimension, y=metric, data=df_combined, marker='o', label='Observed')
    sns.lineplot(x=time_dimension, y=metric, data=df_future, marker='o', linestyle='--', label='Forecast')

    # Hiển thị phương trình hồi quy trên đường dự báo
    regression_equation = f"y = {slope:.2f}x + {intercept:.2f}"
    # Tính góc của đường hồi quy với trục x
    angle = np.degrees(np.arctan(slope))

    plt.text(x=df_future[time_dimension].iloc[len(df_future)//2], 
             y=df_future[metric].iloc[len(df_future)//2], 
             s=regression_equation, 
             fontsize=12, color='red', 
             ha='center', 
             rotation=angle)

    plt.title('Trend Analysis with Forecast', fontsize=16)
    plt.xlabel(time_dimension, fontsize=12)
    plt.ylabel(metric, fontsize=12)
    plt.grid(True)
    plt.legend()

    # Vẽ bảng phân tích với cột thứ 3 là chú thích
    plt.subplot(2, 1, 2)
    plt.axis('off')
    # Điều chỉnh tỷ lệ chiều ngang của các cột
    col_widths = [0.25, 0.15, 0.6]  # Tỷ lệ chiều ngang của các cột (20%, 20%, 60%)

    tbl = plt.table(cellText=analysis_df.values,
                    colLabels=analysis_df.columns,
                    cellLoc='center',
                    colWidths=col_widths,  # Áp dụng tỷ lệ chiều ngang cho các cột
                    loc='center')

    tbl.auto_set_font_size(False)
    tbl.set_fontsize(9)
    tbl.scale(1, 2,5)

    # Tô màu bảng dựa trên giá trị của các biến
    for key, cell in tbl.get_celld().items():
        row_index = key[0]
        col_index = key[1]

        if col_index == 1:  # Cột Value (index 1)
            if row_index == 1:  # Dòng 1 - Mean Absolute Error
                if mae >= 50:
                    cell.set_facecolor('red')
                elif mae >= 30:
                    cell.set_facecolor('yellow')
                else:
                    cell.set_facecolor('lightgreen')
            elif row_index == 2:  # Dòng 2 - Mean Absolute Percentage Error
                if mape * 100 >= 30:
                    cell.set_facecolor('red')
                elif mape * 100 >= 20:
                    cell.set_facecolor('yellow')
                else:
                    cell.set_facecolor('lightgreen')
            elif row_index == 3:  # Dòng 3 - p-value
                if p_value <= 0.001:
                    cell.set_facecolor('lightgreen')
                elif p_value <= 0.01:
                    cell.set_facecolor('yellow')
                elif p_value <= 0.05:
                    cell.set_facecolor('lightpink')
                else:
                    cell.set_facecolor('red')  # hoặc giữ màu mặc định
            elif row_index == 4:  # Dòng 4 - Slope
                if slope > 2:
                    cell.set_facecolor('lightgreen')
                elif slope >= 0:
                    cell.set_facecolor('yellow')
                else:
                    cell.set_facecolor('red')
            elif row_index == 5:  # Dòng 5 - R-squared
                if r_squared > 0.9:
                    cell.set_facecolor('lightgreen')
                elif r_squared > 0.7:
                    cell.set_facecolor('yellow')
                elif r_squared > 0.4:
                    cell.set_facecolor('orange')
                elif r_squared > 0.2:
                    cell.set_facecolor('lightpink') 
                else:
                    cell.set_facecolor('red')
            elif row_index == 6:  # Dòng 6 - Mean Value
                cell.set_facecolor('white')  # Không có quy tắc đặc biệt
            elif row_index == 7:  # Dòng 7 - Trend
                if trend_analysis == 'Positive':
                    cell.set_facecolor('lightgreen')
                else:
                    cell.set_facecolor('red')

    plt.tight_layout()
    plt.show()

def plot_trend_analysis_seasonality(df, time_dimension, metric, forecast_periods=12, seasonality = 'M'):
    # Đảm bảo cột time_dimension là kiểu datetime
    df[time_dimension] = pd.to_datetime(df[time_dimension])
    # Tạo DataFrame với tất cả các ngày trong khoảng thời gian
    all_dates = pd.date_range(start=df[f'{time_dimension}'].min(), end=df['Date'].max(), freq='D')
    df_all_dates = pd.DataFrame({f'{time_dimension}': all_dates})

    # Kết hợp với dữ liệu gốc
    df = pd.merge(df_all_dates, df, on=f'{time_dimension}', how='left')

    # Điền giá trị thiếu
    df[f'{metric}'] = df[f'{metric}'].fillna(0)

    # Group dữ liệu theo seasonality
    if seasonality == 'M':
        df = df.resample('M', on=time_dimension).mean().reset_index()
    elif seasonality == 'W':
        df = df.resample('W', on=time_dimension).mean().reset_index()
    elif seasonality == 'D':
        df = df.resample('D', on=time_dimension).mean().reset_index()
    elif seasonality == 'Q':
        df = df.resample('Q', on=time_dimension).mean().reset_index()

    # Bước 1: Chuẩn bị dữ liệu để dự đoán
    df['Date_numeric'] = np.arange(len(df))

    # Thêm các biến mùa vụ nếu cần
    seasonality_df = pd.DataFrame()
    if seasonality == 'W':  # Mùa vụ hàng tuần
        df['Day_of_week'] = df[time_dimension].dt.dayofweek  # 0 = Monday, 6 = Sunday
        enc = OneHotEncoder(sparse_output=False, drop='first', handle_unknown='ignore')
        seasonality_features = enc.fit_transform(df[['Day_of_week']])
        expected_columns = 6  # Expecting 6 columns (one for each day of the week, except one)
    elif seasonality == 'M':  # Mùa vụ hàng tháng
        df['Month'] = df[time_dimension].dt.month
        enc = OneHotEncoder(sparse_output=False, drop='first', handle_unknown='ignore')
        seasonality_features = enc.fit_transform(df[['Month']])
        expected_columns = 11  # Expecting 11 columns (one for each month, except one)
    elif seasonality == 'Q':  # Mùa vụ theo quý
        df['Quarter'] = df[time_dimension].dt.quarter  # Chuyển đổi thành số quý (1, 2, 3, 4)
        enc = OneHotEncoder(categories='auto', sparse_output=False, drop='first', handle_unknown='ignore')
        seasonality_features = enc.fit_transform(df[['Quarter']])
        expected_columns = 3  # Expecting 3 columns (one for each quarter, except one)
    else:
        seasonality_features = np.empty((len(df), 0))  # No seasonality features
        expected_columns = 0

    # Đảm bảo số lượng cột của seasonality_features khớp với mong đợi
    if seasonality_features.shape[1] != expected_columns:
        seasonality_features = np.zeros((len(df), expected_columns))

    seasonality_df = pd.DataFrame(seasonality_features, 
                                  columns=[f'{seasonality}_Feature_{i}' for i in range(1, expected_columns + 1)])

    X = pd.concat([df[['Date_numeric']].reset_index(drop=True), seasonality_df.reset_index(drop=True)], axis=1)

    y = df[metric]

    # Tạo mô hình hồi quy tuyến tính
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Tính các chỉ số hồi quy
    intercept = model.intercept_
    coefficients = model.coef_
    slope = coefficients[0]
    r_squared = model.score(X, y)
    mae = mean_absolute_error(y, y_pred)
    # Tính MAPE chỉ với các giá trị khác 0
    mape = mean_absolute_percentage_error(y[y != 0], y_pred[y != 0])

    # Thêm hệ số chặn vào mô hình để tính p-value
    X_with_const = sm.add_constant(X)
    model_sm = sm.OLS(y, X_with_const)
    results = model_sm.fit()
    p_value = results.pvalues['Date_numeric']

    # Phân tích dựa vào hồi quy
    mean_value = df[metric].mean()
    trend_analysis = "Positive" if slope > 0 else "Negative"

    # Tạo bảng phân tích với cột chú thích thứ 3
   # Fixing the issue with formatting
    analysis_data = {
        'Metric': ['Mean Absolute Error', 'Mean Absolute Percentage Error', 'p_value', 'Slope', 'R-squared', 'Mean Value', 'Trend'],
        'Value': [
            f"{mae:.2f}" if isinstance(mae, float) else str(mae), 
            f"{mape*100:.2f}%" if isinstance(mape, float) else str(mape),
            f"{p_value:.6f}" if isinstance(p_value, float) else str(p_value), 
            f"{slope:.2f}" if isinstance(slope, float) else str(slope),
            f"{r_squared:.5f}" if isinstance(r_squared, float) else str(r_squared),
            f"{mean_value:.2f}" if isinstance(mean_value, float) else str(mean_value),
            trend_analysis
        ],
        'Comment': [
            f'Predictions deviate by {mae:.2f} units from actual values on average',
            f'Prediction errors average {mape*100:.2f}% of the actual values',
            f'The result is {"Very significant" if p_value <= 0.001 else "Strongly significant" if p_value <= 0.01 else "Significant" if p_value <= 0.05 else "Weakly significant" if p_value <= 0.1 else "Not significant"} in predicted',
            f'The slope of {slope:.2f} establishes an {"increasing" if slope > 0 else "decreasing"} trend, \n with the value in the y column {"increasing" if slope > 0 else "decreasing"} by {abs(slope):.2f} units each month',
            f'The r-squared is {r_squared:.5f} and is evaluated as {"excellent" if r_squared > 0.9 else "very good" if r_squared > 0.7 else "good" if r_squared > 0.5 else "average" if r_squared > 0.3 else "poor"} correlation',
            'Average value over time period',
            f'Indicates {trend_analysis} trend'
        ]
    }
    analysis_df = pd.DataFrame(analysis_data)

    # Tạo dự đoán cho tương lai
    future_dates = pd.date_range(start=df[time_dimension].iloc[-1] + pd.DateOffset(1), periods=forecast_periods, freq=seasonality)
    future_dates_numeric = np.arange(len(df), len(df) + len(future_dates))

    if seasonality == 'W':  # Mùa vụ hàng tuần
        future_day_of_week = [d.dayofweek for d in future_dates]
        future_seasonality_features = enc.transform(np.array(future_day_of_week).reshape(-1, 1))
    elif seasonality == 'M':  # Mùa vụ hàng tháng
        future_month = [d.month for d in future_dates]
        future_seasonality_features = enc.transform(np.array(future_month).reshape(-1, 1))
    elif seasonality == 'Q':  # Mùa vụ theo quý
        future_quarter = [d.quarter for d in future_dates]
        future_seasonality_features = enc.transform(np.array(future_quarter).reshape(-1, 1))
    else:  # Không có mùa vụ hoặc hàng ngày
        future_seasonality_features = np.zeros((forecast_periods, 0))

    # Đảm bảo số cột phù hợp với mong đợi
    if future_seasonality_features.shape[1] != expected_columns:
        future_seasonality_features = np.zeros((forecast_periods, expected_columns))

    X_future = np.column_stack([future_dates_numeric, future_seasonality_features])
    future_values = model.predict(X_future)

    # Tạo DataFrame cho dữ liệu dự đoán
    df_future = pd.DataFrame({time_dimension: future_dates, metric: future_values})

    # Kết hợp dữ liệu gốc và dữ liệu dự đoán
    df_combined = pd.concat([df, df_future])

    # Bước 3: Vẽ biểu đồ xu hướng với dự đoán tương lai và bảng phân tích
    fig, ax = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [3, 1]})

    # Vẽ biểu đồ xu hướng với màu mặc định của seaborn
    sns.lineplot(x=time_dimension, y=metric, data=df_combined, marker='o', ax=ax[0], label='Observed')
    sns.lineplot(x=time_dimension, y=metric, data=df_future, marker='o', linestyle='--', ax=ax[0], label='Forecast')

    # Thêm vạch đỏ tại điểm bắt đầu dự đoán
    ax[0].axvline(x=df[time_dimension].iloc[-1], color='red', linestyle='--', label='Forecast Start')
    
    ax[0].set_title(f'{metric} Trend Analysis with Forecast')
    ax[0].set_xlabel(time_dimension)
    ax[0].set_ylabel(metric)
    ax[0].legend()
    ax[0].grid(True)

    # Vẽ bảng phân tích phía dưới biểu đồ
    ax[1].axis('tight')
    ax[1].axis('off')
    col_widths = [0.25, 0.15, 0.6]
    table = ax[1].table(cellText=analysis_df.values, colLabels=analysis_df.columns, loc='center', cellLoc='left', colLoc='left', colWidths=col_widths)
    table.scale(1, 2.5)
    # Tô màu bảng dựa trên giá trị của các biến
    for key, cell in table.get_celld().items():
        row_index = key[0]
        col_index = key[1]

        if col_index == 1:  # Cột Value (index 1)
            if row_index == 1:  # Dòng 1 - Mean Absolute Error
                if mae >= 50:
                    cell.set_facecolor('red')
                elif mae >= 30:
                    cell.set_facecolor('yellow')
                else:
                    cell.set_facecolor('lightgreen')
            elif row_index == 2:  # Dòng 2 - Mean Absolute Percentage Error
                if mape * 100 >= 30:
                    cell.set_facecolor('red')
                elif mape * 100 >= 20:
                    cell.set_facecolor('yellow')
                else:
                    cell.set_facecolor('lightgreen')
            elif row_index == 3:  # Dòng 3 - p-value
                if p_value <= 0.001:
                    cell.set_facecolor('lightgreen')
                elif p_value <= 0.01:
                    cell.set_facecolor('yellow')
                elif p_value <= 0.05:
                    cell.set_facecolor('lightpink')
                else:
                    cell.set_facecolor('red')  # hoặc giữ màu mặc định
            elif row_index == 4:  # Dòng 4 - Slope
                if slope > 2:
                    cell.set_facecolor('lightgreen')
                elif slope >= 0:
                    cell.set_facecolor('yellow')
                else:
                    cell.set_facecolor('red')
            elif row_index == 5:  # Dòng 5 - R-squared
                if r_squared > 0.9:
                    cell.set_facecolor('lightgreen')
                elif r_squared > 0.7:
                    cell.set_facecolor('yellow')
                elif r_squared > 0.4:
                    cell.set_facecolor('orange')
                elif r_squared > 0.2:
                    cell.set_facecolor('lightpink') 
                else:
                    cell.set_facecolor('red')
            elif row_index == 6:  # Dòng 6 - Mean Value
                cell.set_facecolor('white')  # Không có quy tắc đặc biệt
            elif row_index == 7:  # Dòng 7 - Trend
                if trend_analysis == 'Positive':
                    cell.set_facecolor('lightgreen')
                else:
                    cell.set_facecolor('red')

    plt.tight_layout()
    plt.show()
