import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
iris = sns.load_dataset('iris')

# Create pairplot
sns.pairplot(iris, hue='species')

plt.suptitle('Pairplot - Iris Dataset', y=1.02)
plt.tight_layout()
plt.show()

