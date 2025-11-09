import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
df = pd.read_csv('./assets/Medical_Data_Dataset.csv')
# sns.boxplot(x='age', y='bmi', data=df, palette='winter')
# plt.show()
high_charges = df[df['charges'] > 60000]
print(high_charges)
# Function to calculate whiskers
def wisker(col):
    q1, q3 = np.percentile(col, [25, 75])
    IQR = q3 - q1
    lw = q1 - 1.5 * IQR  # Lower Whisker
    uw = q3 + 1.5 * IQR  # Upper Whisker
    return lw, uw

# Treating continuous variables with outliers
columns_to_treat = ['age','bmi']

for col in columns_to_treat:
    sns.boxplot(data=df, x=col)
    plt.title(f'Boxplot of {col}')
    plt.show()
# First remove extra spaces from column names (if any)
df.columns = df.columns.str.strip()

for col in columns_to_treat:
    lw, uw = wisker(df[col])
    df[col] = np.where(df[col] < lw, lw, df[col])
    df[col] = np.where(df[col] > uw, uw, df[col])

# Plot boxplots after treating outliers
for col in columns_to_treat:
    sns.boxplot(data=df, x=col)
    plt.title(f'Boxplot of {col}')
    plt.show()