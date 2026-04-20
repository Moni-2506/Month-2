
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Basic inspection
print("\nINFO:\n")
print(df.info())

print("\nDESCRIBE:\n")
print(df.describe(include='all'))

print("\nMissing Values:\n")
print(df.isnull().sum())