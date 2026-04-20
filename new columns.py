
import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv("cleaned_input.csv")

# --- Tenure Grouping ---
def tenure_group(tenure):
    if tenure <= 12:
        return "0-12"
    elif tenure <= 24:
        return "13-24"
    elif tenure <= 36:
        return "25-36"
    elif tenure <= 48:
        return "37-48"
    elif tenure <= 60:
        return "49-60"
    else:
        return "60+"

df['TenureGroup'] = df['tenure'].apply(tenure_group)

# --- Avg Monthly Spend ---
df['AvgMonthlySpend'] = df['TotalCharges'] / df['tenure']

# Avoid division issues
df['AvgMonthlySpend'].replace([np.inf, -np.inf], np.nan, inplace=True)
df['AvgMonthlySpend'].fillna(df['MonthlyCharges'], inplace=True)

# --- Convert Yes/No → 1/0 ---
binary_cols = df.select_dtypes(include='object').columns

for col in binary_cols:
    if set(df[col].dropna().unique()) <= {"Yes", "No"}:
        df[col] = df[col].map({"Yes": 1, "No": 0})

# --- One-hot Encoding ---
categorical_cols = ['Contract', 'InternetService', 'PaymentMethod']

df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

print("Feature Engineering Done")
print(df.head())