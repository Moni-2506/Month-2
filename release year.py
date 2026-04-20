
# Ensure release_year is numeric
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

print(df['release_year'].head())    