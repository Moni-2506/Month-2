
print("\nMissing values:\n")
print(df.isnull().sum())

# Detect blank spaces or weird placeholders
df = df.replace(" ", np.nan)  # replace single space with NaN
df = df.replace("", np.nan)   # replace empty string

# Check again
print("\nMissing after cleaning blanks:\n")
print(df.isnull().sum())