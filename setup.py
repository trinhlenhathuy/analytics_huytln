# Cập nhật lại file setup.py để thêm phần mô tả dài (long_description) từ README.md

setup_content = """
from setuptools import setup, find_packages

# Đọc nội dung của README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='analytics_huytln',
    version='0.2.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
    ],
    description='A simple library to plot Insightful charts',
    long_description=long_description,  # Thêm mô tả dài
    long_description_content_type="text/markdown",  # Định dạng của README.md
    author='Huy Trịnh Lê Nhật',
    author_email='trinhlenhathuy@gmail.com',
    # url='https://github.com/trinhlenhathuy/analytics_huytln',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
"""

# Lưu nội dung đã chỉnh sửa vào file setup.py
with open("/mnt/data/setup.py", "w", encoding="utf-8") as file:
    file.write(setup_content)
