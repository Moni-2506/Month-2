
df['content_type'] = df['type'].apply(
    lambda x: "Movie" if x == "Movie" else "TV Show"
)

print(df[['type', 'content_type']].head())