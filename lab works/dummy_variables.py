import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# df = pd.read_csv('./assets/carprices.csv')
# print(df.columns)
# dummy = pd.get_dummies(df['Car Model'])
# merge = pd.concat([df, dummy],axis = 1)
# # print(merge)
# res = merge.drop(['Car Model'],axis = 1)
# print(res)
# Bivariate analysis
# Numerical Vs NUMERICAL
iris_df = pd.read_csv('./assets/iris.csv')
# print(iris_df.describe())
# sns.scatterplot(x='sepal_length',y='sepal_width', data = iris_df, hue = 'species')
# plt.show()


#Categorical vs numerical analysis
# iris_df = pd.read_csv('./assets/tips.csv')
# print(iris_df.describe())
# print(iris_df.info())
# print(iris_df.columns)
# sns.catplot(x='sex',y='tip', data = iris_df, hue = 'smoker', kind='strip', col='time')
# Kind attributes: swarm , point , strip , box

# plt.show()

# Pair plot - metrix form of plotting
sns.pairplot(iris_df, hue = 'species', diag_kind = 'hist')
plt.show()