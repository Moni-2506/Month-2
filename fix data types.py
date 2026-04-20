
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

print("\nUpdated dtypes:\n")
print(df.dtypes)