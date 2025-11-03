# UK-House-Price-Analytics-Forecasting-Dashboard-Power-BI-Python-

UK House Price Analytics & Forecasting Dashboard

Power BI · Python · UK House Price Index (HPI)

This project provides an end-to-end analysis of the UK housing market using the official UK House Price Index (HPI) dataset.
It includes:

✅ Data cleaning & preprocessing (Python)
✅ Exploratory analysis (Python)
✅ A full Power BI interactive dashboard
✅ Monthly trend analysis
✅ Geospatial housing price map
✅ YoY/MoM growth metrics
✅ Time-series forecasting using Power BI Analytics

This project is designed to reflect the workflow of a real data analyst / data scientist working in the UK.

📊 Dashboard Preview

The Power BI dashboard includes:

UK house price overview

Regional comparison

YoY & MoM growth

Geospatial map of average price by region

Trend charts from 2010–2024

12-month forecast

The .pbix file is included in /powerbi_dashboard/.

📁 Project Structure
uk-house-price-analysis/
│
├── data/
│   ├── raw/               # Original dataset
│   └── processed/         # Cleaned dataset
│
├── src/
│   ├── data_cleaning.py   # Python ETL script
│   ├── modeling.py        # Optional regression models
│   └── utils.py
│
├── powerbi_dashboard/
│   └── UK_House_Price_Dashboard.pbix
│
└── README.md

📥 Dataset

This project uses the UK Government UK House Price Index (HPI) dataset:

Monthly average price

By country / region / local authority

1995–2024

The dataset is available under the Open Government Licence.

🧹 Data Cleaning (Python)

The cleaning process includes:

Parsing dates

Converting price columns to numeric

Generating Year / Month columns

Handling missing values

Aggregating average price by region

Exporting to processed/hpi_cleaned.csv

Run:

python src/data_cleaning.py

📈 Modeling (Regression)

A simple regression model (Linear Regression & Random Forest) is included as an optional module.

Run:

python src/modeling.py

📊 Power BI Dashboard
Dashboard Pages
✅ Page 1 – UK Overview

Card: Latest UK average price

Line chart: UK monthly price trend (2010–2024)

Bar chart: Average price by region

Slicer: Region selector

✅ Page 2 – Geospatial Map

Filled Map: Average price by region/local authority

Tooltip: YoY change + average price

✅ Page 3 – Growth & Trend Analysis

YoY % Growth line chart

MoM % Growth

Top 10 fastest-growing regions (bar chart)

✅ Page 4 – Forecast

Line Chart with Power BI “Forecast” Analytics

12-month prediction

Confidence interval shown

🛠️ Technologies

Python (Pandas, NumPy, Scikit-learn)

Power BI (Power Query, DAX, Forecast Analytics)

Git / GitHub

📌 Author

Tyler Chan
Data Science & Big Data Technology
University of Bristol (MSc Data Science Offer Holder)
