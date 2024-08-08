from setuptools import setup, find_packages

setup(
    name='pareto_chart_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
    ],
    description='A simple library to plot Pareto charts',
    author='Huy Trịnh Lê Nhật',
    author_email='trinhlenhathuy@gmail.com',
    # url='https://github.com/trinhlenhathuy/huytln_visualization',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
