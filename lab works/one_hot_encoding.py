import pandas as pd
# Load the dataset (separator is usually ';' in this dataset)
df = pd.read_csv("./assets/bank-additional-full.csv", sep=';')

# Preview the dataset
print(df.head())
# Select only object-type (categorical) columns
categorical_cols = df.select_dtypes(include=['object']).columns

print("Categorical columns:")
print(categorical_cols)
# Apply one-hot encoding while dropping the first category to avoid multicollinearity
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Display the transformed DataFrame
print("Transformed DataFrame")
print(df_encoded.head())
