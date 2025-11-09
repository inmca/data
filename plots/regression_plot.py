import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
iris = sns.load_dataset('iris')

# Create regression plot
sns.regplot(x='sepal_length', y='petal_length', data=iris, scatter=True, fit_reg=True)

# Add labels and title
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Regression Plot - Iris Dataset')

plt.tight_layout()
plt.show()

