import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv('./assets/iris.csv')

# Create histogram
plt.hist(df['sepal_length'], bins=30, color='skyblue', alpha=0.7, edgecolor='black')

# Add labels and title
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

