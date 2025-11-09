import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
df = pd.read_csv('./assets/iris.csv')

# Create pairplot
sns.pairplot(df, hue='species')

plt.suptitle('Pairplot', y=1.02)
plt.tight_layout()
plt.show()

