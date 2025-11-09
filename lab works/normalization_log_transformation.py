import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('./assets/winequality-white-1.csv')
print(df.columns)
sns.histplot(data=df,x='free sulfur dioxide')
plt.show()

# Max absolute normalization method
df_copy = df.copy()
df_copy['free sulfur dioxide'] = df_copy['free sulfur dioxide']/df_copy['free sulfur dioxide'].abs().max()
# sns.histplot(df_copy['free sulfur dioxide'])
# plt.show()

#Method 2 norm --> [(value-min)/(max-min)]
# df_copy['free sulfur dioxide'] = df_copy['free sulfur dioxide']-df_copy['free sulfur dioxide']/df_copy['free sulfur dioxide'].abs().max()-df_copy['free sulfur dioxide'].abs().min()


# Transforming data(log transformation)
# sns.displot(df_copy['total sulfur dioxide'], kde = True)
df_copy['total sulfur dioxide'] = np.log(df_copy['total sulfur dioxide']+1)
sns.displot(df_copy['total sulfur dioxide'], kde = True)
plt.show()