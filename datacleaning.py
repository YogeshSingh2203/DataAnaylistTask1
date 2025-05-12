import pandas as pd

# Load the data using the correct delimiter (tab-separated)
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# Clean column names by stripping spaces, converting to lowercase, and replacing spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Print available columns to verify they are correctly parsed
print("Available columns:", df.columns)

# 1. Handle the Missing Values (Check for missing values in the 'income' column)
if 'income' in df.columns:
    missing_income = df['income'].isnull().sum()  # Count the missing values in 'income'
    print(f"Missing 'Income' values: {missing_income}")
    # Replace missing 'income' values with the median value of the column
    df['income'] = df['income'].fillna(df['income'].median())  # No 'inplace' here
else:
    print("The 'income' column is not present in the dataset.")

# 2. Standardize Text Columns (education, marital_status)
if 'education' in df.columns:
    df['education'] = df['education'].str.strip().str.capitalize()

if 'marital_status' in df.columns:
    df['marital_status'] = df['marital_status'].str.strip().str.capitalize()
    # Replace specific values in 'marital_status'
    df['marital_status'] = df['marital_status'].replace({
        'Alone': 'Single',
        'Absurd': 'Other',
        'Yolo': 'Other'
    })

# 3. Convert 'dt_customer' column to datetime format
if 'dt_customer' in df.columns:
    df['dt_customer'] = pd.to_datetime(df['dt_customer'], format='%d-%m-%Y')

# 4. Rename columns to lowercase and replace spaces with underscores
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# 5. Remove duplicates
df.drop_duplicates(inplace=True)

# 6. Remove future or unrealistic birth years (birth year >= 1940)
df = df[df['year_birth'] >= 1940]

# 7. Save the cleaned dataset to a new CSV file
df.to_csv("cleaned_marketing_campaign.csv", index=False)

# Optional: Display the first few rows of the cleaned data
print(df.head())
