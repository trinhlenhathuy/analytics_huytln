from setuptools import setup, find_packages

# Đọc nội dung của README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='analytics_huytln',
    version='0.2.2',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
    ],
    description='A simple library to plot insightful charts',
    long_description=long_description,  # Thêm mô tả dài
    long_description_content_type="text/markdown",  # Định dạng của README.md
    author='Huy Trịnh Lê Nhật',
    author_email='trinhlenhathuy@gmail.com',
    url='https://github.com/trinhlenhathuy/huytln_visualization',  # URL dự án
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',  # Giấy phép của dự án
    keywords='data visualization, charts, pareto, heatmap',  # Từ khóa tìm kiếm
)
