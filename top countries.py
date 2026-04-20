
# Split multiple countries
df['country'] = df['country'].fillna("Unknown")
df['country'] = df['country'].apply(lambda x: x.split(", "))

# Explode into separate rows
df_country = df.explode('country')

# Get top 5 countries
top_countries = df_country['country'].value_counts().head(5)

print("\nTop 5 Countries:\n")
print(top_countries)