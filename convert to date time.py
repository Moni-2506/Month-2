
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Extract useful time features
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

print(df[['date_added', 'year_added', 'month_added']].head())