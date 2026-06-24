# Student Data Analysis with Pandas

This project is a simple Python script built using the Pandas library to handle and clean academic data. It focuses on structuring a DataFrame, changing data types, and handling missing or null values (NaN).

## Features
The `pandas_data_analysis.py` script performs the following operations:
1. **DataFrame Creation**: Builds a dataset containing academic majors, course names, and level numbers.
2. **Data Description**: Utilizes `df.describe()` to generate quick descriptive statistics of the dataset.
3. **Data Type Conversion**: Casts the `Level` column into floating-point numbers (`float`).
4. **Data Cleaning**: Uses `df.dropna(how='all')` to filter out rows where all elements are missing or empty (`NaN`).

## Tech Stack
* Python 3.x
* Pandas Library

## Getting Started

### Prerequisites
Make sure you have Python installed, then install the required Pandas library using your terminal:
```bash
pip install pandas
