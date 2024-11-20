# Submission Data Analysis - Bike Rental 🚴‍♂️
This project conducts an analysis of bike rental data using Python, leveraging libraries such as Pandas, NumPy, Matplotlib, Seaborn, and SciPy to explore trends and insights from two datasets: day.csv and hour.csv.

## Project Description
This project involves processing and analyzing data to understand patterns and trends in bike rentals, including the effects of seasonality, weather conditions, and holidays on rental numbers.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Google Collab
- 
## Environment Setup
Dataset
```
- data/
    - day.csv
    - hour.csv
```

## Project Structure

|-- dashboard/

    |-- Dashboard.py
    
|-- data/

    |-- day.csv
    
    |-- hour.csv
    
    |-- README.txt
    
|-- DataAnalystSubmission.ipynb

|-- README.md

|-- requirements.txt

## Analysis Workflow
The workflow of the project can be divided into the following steps:
1. Data Loading
Load the day.csv and hour.csv datasets into Pandas DataFrames for analysis. This step involves reading the data files and preparing them for further processing.
2. Data Cleaning
Handle Missing Values: Identify and fill missing values if present, or remove rows/columns with missing data, depending on the context.
Convert Data Types: Ensure that columns such as dates, times, or categories are converted to their appropriate data types (e.g., converting date columns into datetime format).
Handle Outliers: Detect any anomalies or extreme outliers in the data, and decide whether to remove them or cap their values.
3. Exploratory Data Analysis (EDA)
EDA helps in understanding the underlying patterns, trends, and relationships in the data.
4. Data Visualization & Explanatory Analysis
Visualization is key to revealing insights that may not be immediately obvious from raw data.
Bar Charts: Display categorical data comparisons, such as bike rentals by season or day of the week.
Explanatory analysis dives deeper into why certain patterns are emerging from the data.

