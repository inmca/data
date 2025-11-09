import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv('./assets/iris.csv')

# Calculate mean sepal length by species
data = df.groupby('species')['sepal_length'].mean()

# Create bar plot
plt.bar(data.index, data.values, color='steelblue', alpha=0.7)

# Add labels and title
plt.xlabel('Species')
plt.ylabel('Mean Sepal Length')
plt.title('Bar Plot')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

