import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('./assets/iris.csv')

# Calculate mean values by species
species_means = df.groupby('species').agg({
    'sepal_length': 'mean',
    'petal_length': 'mean'
})

x = np.arange(len(species_means.index))

# Create area plot
plt.fill_between(x, 0, species_means['sepal_length'], alpha=0.5, label='Sepal Length', color='blue')
plt.fill_between(x, species_means['sepal_length'], species_means['sepal_length'] + species_means['petal_length'], 
                 alpha=0.5, label='Petal Length', color='red')

# Add labels, title, and legend
plt.xlabel('Species')
plt.ylabel('Mean Length (cm)')
plt.title('Area Plot')
plt.xticks(x, species_means.index)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

