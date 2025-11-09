import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv('./assets/iris.csv')

# Create scatter plot
plt.scatter(df['sepal_length'], df['petal_length'], alpha=0.6, c='coral', s=50)

# Add labels and title
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Scatter Plot')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

