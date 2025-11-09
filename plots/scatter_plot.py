import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
iris = sns.load_dataset('iris')

# Create scatter plot
plt.scatter(iris['sepal_length'], iris['petal_length'], alpha=0.6, c='coral', s=50)

# Add labels and title
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Scatter Plot - Iris Dataset')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

