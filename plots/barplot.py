import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
iris = sns.load_dataset('iris')

# Calculate mean sepal length by species
data = iris.groupby('species')['sepal_length'].mean()

# Create bar plot
plt.bar(data.index, data.values, color='steelblue', alpha=0.7)

# Add labels and title
plt.xlabel('Species')
plt.ylabel('Mean Sepal Length')
plt.title('Bar Plot - Iris Dataset')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

