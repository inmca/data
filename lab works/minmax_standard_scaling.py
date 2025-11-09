import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler
df = pd.read_csv('./assets/winequality-white.csv',sep=';')  # CSV uses semicolon as separator

# Preview
print(df.head())

# Select only numerical columns
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Initialize scalers
min_max_scaler = MinMaxScaler()
standard_scaler = StandardScaler()

# Apply Min-Max Scaling
min_max_scaled = pd.DataFrame(min_max_scaler.fit_transform(numeric_df), columns=numeric_df.columns)

# Apply Standardization
standard_scaled = pd.DataFrame(standard_scaler.fit_transform(numeric_df), columns=numeric_df.columns)

plt.figure(figsize=(15, 5))

# Original
plt.subplot(1, 3, 1)
sns.histplot(numeric_df['alcohol'], kde=True, color='blue')
plt.title('Original: alcohol')

# Min-Max
plt.subplot(1, 3, 2)
sns.histplot(min_max_scaled['alcohol'], kde=True, color='green')
plt.title('Min-Max Scaled: alcohol')

# Standardized
plt.subplot(1, 3, 3)
sns.histplot(standard_scaled['alcohol'], kde=True, color='red')
plt.title('Standardized: alcohol')

plt.tight_layout()
plt.show()



