import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
iris = sns.load_dataset('iris')

# Create distribution plot
sns.histplot(iris['petal_length'], kde=True, bins=30, color='purple')

# Add labels and title
plt.xlabel('Petal Length')
plt.ylabel('Density')
plt.title('Distribution Plot - Iris Dataset')

plt.tight_layout()
plt.show()

