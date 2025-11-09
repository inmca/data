import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.core.property.color import Alpha

# Importing Data sets

df = pd.read_csv('assets/titanic_train.csv')
print(df.shape)

# To indentify missing values using a heat map

# sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
# plt.show()

# To find the number of passengers who are survived
# sns.countplot(x='Survived', hue='Sex', data=df,palette='RdBu_r')
# plt.show()

#Histogram plot to identify the distribution of certain attribute using kernel density estimator(KDE)

# sns.histplot(df['Age'], color='Darkred', kde=True, alpha=.7)
# plt.show()

# EDA to find percentile age  having Median age of each passenger class

# sns.boxplot(x='Pclass', y='Age', hue='Sex', data=df, palette='winter')
# plt.show()

# Imputation based on Age attribute with null values using median of age
def impute_age(cols):
    Age = cols[0]
    Pclass=cols[1]
    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 28
        else:
            return 24

    else:
        return Age

df['Age']=df[['Age','Pclass']].apply(impute_age, axis=1)
sns.heatmap(df.isnull(), cbar=False,yticklabels=False, cmap='YlGnBu')
plt.show()