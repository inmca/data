import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
iris = sns.load_dataset('iris')

# Create histogram
plt.hist(iris['sepal_length'], bins=30, color='skyblue', alpha=0.7, edgecolor='black')

# Add labels and title
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title('Histogram - Iris Dataset')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

