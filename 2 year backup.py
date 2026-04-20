
from sklearn.linear_model import LinearRegression
import numpy as np

# Prepare data
yearly = df['release_year'].value_counts().sort_index().reset_index()
yearly.columns = ['year', 'count']

X = yearly['year'].values.reshape(-1,1)
y = yearly['count'].values

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next 2 years
future_years = np.array([yearly['year'].max()+1, yearly['year'].max()+2]).reshape(-1,1)
predictions = model.predict(future_years)

print("\nFuture Predictions:")
for year, pred in zip(future_years.flatten(), predictions):
    print(f"{year}: {int(pred)} titles (estimated)")

# Plot
plt.figure(figsize=(10,5))
plt.plot(yearly['year'], yearly['count'], label="Actual", marker='o')
plt.plot(future_years, predictions, 'ro--', label="Predicted")

plt.legend()
plt.title("Content Trend Prediction")
plt.savefig("prediction.png")
plt.show()