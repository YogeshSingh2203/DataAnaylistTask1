# DataAnaylistTask1

Customer Personality Analysis – Data Cleaning
This project focuses on preparing the Customer Personality Analysis dataset for further analysis through various data cleaning tasks.

Dataset Information:
File Name: marketing_campaign.csv

Source: Kaggle

Key Columns:
Column Name	Description
ID	Unique customer identifier
Year_Birth	Year of birth of the customer
Education	Customer's education level
Marital_Status	Marital status (e.g., Married, Single)
Income	Annual household income
Dt_Customer	Date when the customer registered
Recency	Days since the customer made their last purchase
MntWines	Amount spent on wine
MntMeatProducts	Amount spent on meat products
NumWebPurchases	Number of purchases made via the website

Cleaning Steps Performed:
Handled Missing Values:

Replaced missing values in the Income column with the median income.

Removed Unrealistic Data:

Removed rows where the Year_Birth was earlier than 1940, as they are considered unrealistic.

Standardized Text Columns:

Capitalized text values in Education and Marital_Status columns.

Corrected specific entries in Marital_Status:

"Alone" → "Single"

"Absurd"/"YOLO" → "Other"

Date Conversion:

Converted the Dt_Customer column to a datetime format.

Duplicates:

No duplicate rows were found during the cleaning process.

Files:
marketing_campaign.csv: Original raw dataset

cleaned_marketing_campaign.csv: Cleaned version of the dataset

data_cleaning_customer_personality.py: Python script used for data cleaning

Task 1 Summary-File: Summary of the data cleaning task

README.md: Project documentation explaining the dataset and steps taken

Tools and Libraries Used:
Programming Language: Python

Library: Pandas for data manipulation

File Format: CSV for both raw and cleaned data

This project cleaned and prepped the Customer Personality Analysis dataset for further exploration, providing a robust foundation for analysis and modeling.

