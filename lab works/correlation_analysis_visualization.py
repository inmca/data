import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("./assets/Framingham.csv")

# Preview dataset
print(df.head())
print(df.info())
# Check missing values
print(df.isnull().sum())

# Optional: Drop rows with missing values
df = df.dropna()
# Scatter plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x='BMI', y='sysBP', data=df)
plt.title("Scatter Plot: BMI vs Systolic BP")
plt.show()

# Correlation
correlation = df[['BMI', 'sysBP']].corr()
print("Correlation Matrix:\n", correlation)


plt.figure(figsize=(6, 4))
sns.boxplot(x='TenYearCHD', y='glucose', data=df)
plt.title("Boxplot: Glucose by Heart Disease Status")
plt.show()

# Grouped Mean
grouped_mean = df.groupby('TenYearCHD')['glucose'].mean()
print("Mean Glucose by Heart Disease Status:\n", grouped_mean)
# Cross Tabulation
cross_tab = pd.crosstab(df['education'], df['TenYearCHD'])

# Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(cross_tab, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap: Education vs Heart Disease")
plt.xlabel("Heart Disease (TenYearCHD)")
plt.ylabel("Education Level")
plt.show()