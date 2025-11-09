import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
iris = sns.load_dataset('iris')

# Prepare data for boxplot
data = [iris[iris['species'] == species]['sepal_length'].values for species in iris['species'].unique()]

# Create boxplot
plt.boxplot(data, labels=iris['species'].unique())

# Add labels and title
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.title('Boxplot - Iris Dataset')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

