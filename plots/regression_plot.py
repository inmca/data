import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
df = pd.read_csv('./assets/iris.csv')

# Create regression plot
sns.regplot(x='sepal_length', y='petal_length', data=df, scatter=True, fit_reg=True)

# Add labels and title
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Regression Plot')

plt.tight_layout()
plt.show()

