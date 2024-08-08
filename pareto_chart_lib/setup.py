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
    author='Your Name',
    author_email='your_email@example.com',
)