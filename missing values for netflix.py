
# Fill missing values for categorical columns
df['director'].fillna("Unknown", inplace=True)
df['cast'].fillna("Not Available", inplace=True)
df['country'].fillna("Unknown", inplace=True)

# Optional: Drop rows where critical columns are missing
df.dropna(subset=['date_added'], inplace=True)

print("\nMissing After Cleaning:\n")
print(df.isnull().sum())