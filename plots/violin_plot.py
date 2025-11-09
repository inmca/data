import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
iris = sns.load_dataset('iris')

# Create violin plot
sns.violinplot(x='species', y='sepal_length', data=iris)

# Add labels and title
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.title('Violin Plot - Iris Dataset')

plt.tight_layout()
plt.show()

