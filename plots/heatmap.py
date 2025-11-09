import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
iris = sns.load_dataset('iris')

# Calculate correlation matrix
corr = iris.select_dtypes(include=['float64']).corr()

# Create heatmap
sns.heatmap(corr, annot=True, fmt='.2f', cmap='viridis', cbar=True)

# Add title
plt.title('Heatmap - Iris Dataset Correlation')
plt.tight_layout()
plt.show()

