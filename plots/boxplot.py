import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv('./assets/iris.csv')

# Prepare data for boxplot
data = [df[df['species'] == species]['sepal_length'].values for species in df['species'].unique()]

# Create boxplot
plt.boxplot(data, labels=df['species'].unique())

# Add labels and title
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.title('Boxplot')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

