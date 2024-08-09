from setuptools import setup, find_packages

setup(
    name='analytics_huytln',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
    ],
    description='A simple library to plot Insightful charts',
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
