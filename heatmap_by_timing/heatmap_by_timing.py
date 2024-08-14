import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap_by_timing(df, dim_name, metric, highlight):
    """
    Hàm để tạo biểu đồ Sales theo thời gian và SKU, với các điểm lớn nhất được tô màu.
    
    Args:
    df: DataFrame chứa dữ liệu.
    dim_name: Tên cột đại diện cho SKU.
    metric: Tên cột đại diện cho Sales.
    highlight: Số lượng điểm lớn nhất cần được highlight.
    """
    # Sắp xếp dữ liệu theo `metric` giảm dần và chọn ra highlight điểm lớn nhất
    top_n = df.nlargest(highlight, metric)

    # Tính tổng số lượng đơn hàng để xác định kích thước điểm
    total_Sales = df[metric].sum()
    sizes = df[metric] / total_Sales * 300

    # Tạo biểu đồ với Seaborn
    plt.figure(figsize=(20, 10))

    # Vẽ các điểm dữ liệu
    scatter = sns.scatterplot(
        x=df['timing'],
        y=df[dim_name],
        size=sizes,
        hue=sizes,
        sizes=(20, 300),
        alpha=0.5,
        palette='viridis',
        legend=False
    )

    # Lấy các nhãn duy nhất của `timing`
    unique_timing = df['timing'].unique()

    # Vẽ các khung hình chữ nhật màu đỏ cho highlight điểm lớn nhất
    for timing in top_n['timing']:
        plt.axvspan(
            timing, timing,
            color='red', alpha=0.3, linewidth=2
        )

    # Tùy chỉnh biểu đồ
    plt.xlabel('Timing')
    plt.ylabel(dim_name)
    plt.title(f'{metric} by Timing and {dim_name}')

    # Hiển thị nhãn trục x, xoay 45 độ và giảm kích thước phông chữ
    plt.xticks(rotation=90, fontsize=6, color='black')

    # Tạo một biểu đồ giả để thêm chú thích màu
    dummy = plt.scatter([], [], c=[], cmap='viridis', s=[], alpha=0.5)
    plt.colorbar(dummy, label=metric)

    # Hiển thị biểu đồ
    plt.show()
