import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
df = pd.read_csv('./assets/iris.csv')

# Calculate correlation matrix
corr = df.select_dtypes(include=['float64']).corr()

# Create heatmap
sns.heatmap(corr, annot=True, fmt='.2f', cmap='viridis', cbar=True)

# Add title
plt.title('Heatmap')
plt.tight_layout()
plt.show()

