
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(14,10))

# --- Pie: Content Type ---
content_counts = df['content_type'].value_counts()
axes[0,0].pie(content_counts, labels=content_counts.index, autopct='%1.1f%%',
              colors=['#4CAF50','#FF7043'])
axes[0,0].set_title("Movies vs TV Shows")

# --- Line: Yearly Trend ---
yearly = df['release_year'].value_counts().sort_index()
axes[0,1].plot(yearly.index, yearly.values, marker='o')
axes[0,1].set_title("Content Trend Over Years")

# --- Top Genres ---
df['listed_in'] = df['listed_in'].apply(lambda x: x.split(", "))
df_genre = df.explode('listed_in')
top_genres = df_genre['listed_in'].value_counts().head(8)

sns.barplot(x=top_genres.values, y=top_genres.index, ax=axes[1,0], palette="viridis")
axes[1,0].set_title("Top Genres")

# --- Country Heatmap ---
df_country = df.copy()
df_country['country'] = df_country['country'].fillna("Unknown")
df_country['country'] = df_country['country'].apply(lambda x: x.split(", "))
df_country = df_country.explode('country')

top_countries = df_country['country'].value_counts().head(5).index
heat_data = pd.crosstab(df_country[df_country['country'].isin(top_countries)]['country'],
                        df_country['content_type'])

sns.heatmap(heat_data, annot=True, fmt='d', cmap='coolwarm', ax=axes[1,1])
axes[1,1].set_title("Country vs Content")

plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()