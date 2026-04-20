
df = df[df['TotalCharges'].notnull()]

# Example: remove negative values (if invalid)
df = df[df['TotalCharges'] >= 0]

# Flag suspicious rows (optional)
df['flag_invalid'] = df['TotalCharges'].isnull()

print("\nFinal dataset shape:", df.shape)