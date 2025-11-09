import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv('./assets/iris.csv')

# Calculate mean values by species
species_means = df.groupby('species')[['sepal_length', 'petal_length']].mean()

# Create line plot
plt.plot(species_means.index, species_means['sepal_length'], label='Sepal Length', color='blue', marker='o', linewidth=2)
plt.plot(species_means.index, species_means['petal_length'], label='Petal Length', color='red', marker='s', linewidth=2)

# Add labels, title, and legend
plt.xlabel('Species')
plt.ylabel('Length (cm)')
plt.title('Line Plot')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

