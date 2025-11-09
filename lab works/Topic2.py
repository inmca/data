import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import KNNImputer

df = pd.read_csv('./assets/Life Expectancy Data.csv')
# print(df.info())
#
# # checking missing values
#
# print(df.isnull().sum()/df.shape[0]*100)
#
# # df.isnull().sum()/df.shape[0]*100 -> to get the percentage of the rows.
# # Finding duplicates
# print(df.duplicated())
#
# # To check whether there is garbage values.
# for i in df.select_dtypes(include = "object").columns:
#     print(df[i].value_counts())

# # Perform exploratory data analysis
# print(df.describe(include="object"))
# # To get the EDA if specified data Type -> include="object"

# # For creating histogram
# for i in df.select_dtypes(include="number").columns:
#     sns.histplot(data=df,x=i)
#     plt.show()


# # For creating boxplot
# for i in df.select_dtypes(include="number").columns:
#     sns.boxplot(data=df,x=i)
#     plt.show()


# # df.describe() -> to get the in [] values
# # To create scatter plot
# for i in ['Country', 'Year', 'Status', 'Adult Mortality',
#        'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B',
#        'Measles ', ' BMI ', 'under-five deaths ', 'Polio', 'Total expenditure',
#        'Diphtheria ', ' HIV/AIDS', 'GDP', 'Population',
#        ' thinness  1-19 years', ' thinness 5-9 years',
#        'Income composition of resources', 'Schooling']:
#     sns.scatterplot(data=df, x=i, y='Life expectancy ')
#     plt.show()

# # For creating heatmap
# corr = df.select_dtypes(include="number").corr()
# print(corr)
# sns.heatmap(corr, annot = True)
# plt.show()

# Treating missing values
# print(df.isnull().sum())
# print(df.columns)
# df[' BMI ']=df[' BMI '].fillna(df[' BMI '].mean())
# print(df.isnull().sum())
#
# df['Polio']=df['Polio'].fillna(df['Polio'].mean())
# print(df.isnull().sum())

# df['GDP']=df['GDP'].fillna(df['GDP'].mode())
# print(df.isnull().sum())

# # Trying to clean the dataset
# df['GDP'].replace(['-','nan','NAN','none',''],np.nan,inplace=True)
# # Convert into numeric values
# df['GDP']=pd.to_numeric(df['GDP'],errors="coerce")
# df['GDP']=df['GDP'].fillna(df['GDP'].mode()[0])
# print(df.isnull().sum())


# Imputing missing values using KNNImputer()

num = df.select_dtypes(include="number").columns
impute = KNNImputer(n_neighbors=5)
df[num] = impute.fit_transform(df[num])
# print(df[num].isnull().sum())



# Treating Outliers

# sns.boxplot(data=df, x="Year", y="Polio")
# plt.show()

# Function to calculate whiskers
def wisker(col):
    q1, q3 = np.percentile(col, [25, 75])
    IQR = q3 - q1
    lw = q1 - 1.5 * IQR  # Lower Whisker
    uw = q3 + 1.5 * IQR  # Upper Whisker
    return lw, uw

# Treating continuous variables with outliers
columns_to_treat = ['GDP', 'Total expenditure', ' thinness  1-19 years', ' thinness 5-9 years']

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

# Replace spaces with underscores in column names
df.columns = df.columns.str.replace(' ', '_')
print(df.columns.tolist())

df.drop_duplicates()





