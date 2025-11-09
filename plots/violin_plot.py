import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
df = pd.read_csv('./assets/iris.csv')

# Create violin plot
sns.violinplot(x='species', y='sepal_length', data=df)

# Add labels and title
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.title('Violin Plot')

plt.tight_layout()
plt.show()

