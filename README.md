# analytics_huytln
# Analytics Huytln

![Python Versions](https://img.shields.io/pypi/pyversions/analytics-huytln)
![License](https://img.shields.io/pypi/l/analytics-huytln)
![PyPI Version](https://img.shields.io/pypi/v/analytics-huytln)

`analytics-huytln` là một thư viện Python được thiết kế để hỗ trợ phân tích dữ liệu qua các biểu đồ và trực quan hóa dữ liệu. Mục tiêu của thư viện này là giúp các nhà phân tích và khoa học dữ liệu dễ dàng hơn trong việc khám phá, phân tích và trình bày dữ liệu của họ.

## Tính năng

- **Phân tích dữ liệu dễ dàng**: Cung cấp các công cụ mạnh mẽ để phân tích dữ liệu với các hàm và phương thức tiện lợi.
- **Tạo biểu đồ**: Hỗ trợ nhiều loại biểu đồ phổ biến để trực quan hóa dữ liệu.
- **Tương thích cao**: Làm việc tốt với các định dạng dữ liệu phổ biến như CSV, Excel, JSON.
- **Dễ sử dụng**: Cung cấp API thân thiện với người dùng, dễ dàng tích hợp vào các dự án hiện có.

## Cài đặt

Cài đặt `analytics-huytln` thông qua pip:

```bash
pip install analytics-huytln


## Hướng dẫn sử dụng

### Hàm `plot_pareto_chart`

Hàm `plot_pareto_chart` tạo biểu đồ Pareto từ dữ liệu Excel.

#### Tham số

- **df** (`pandas.DataFrame`): DataFrame chứa dữ liệu với cột `dim_name` (hạng mục) và `metric` (giá trị).
- **dim_name** (`str`): Tên cột đại diện cho danh mục/hạng mục (ví dụ: SKU).
- **metric** (`str`): Tên cột chứa giá trị cần phân tích (ví dụ: Sales).

#### Sử dụng

Dưới đây là cách sử dụng hàm `plot_pareto_chart`:

```python
import pandas as pd
from analytics_huytln import plot_pareto_chart

# Đọc dữ liệu từ tệp Excel
df = pd.read_excel(r'C:\Users\huytln\Desktop\Linkedln post pdf\data_pareto.xlsx')

# Tạo biểu đồ Pareto
plot_pareto_chart(df, 'SKU', 'Sales')






















git clone https://github.com/trinhlenhathuy/analytics_huytln.git 

cd analytics_huytln

python setup.py sdist bdist_wheel 

twine upload --config-file C:\Users\huytln\analytics_huytln\.pypirc dist/*
