
df['release_decade'] = (df['release_year'] // 10) * 10

print(df[['release_year', 'release_decade']].head())