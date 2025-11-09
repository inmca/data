import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
df = pd.read_csv('./assets/winequality-white-1.csv')

# Create distribution plot
sns.histplot(df['free sulfur dioxide'], kde=True, bins=30, color='purple')

# Add labels and title
plt.xlabel('Free Sulfur Dioxide')
plt.ylabel('Density')
plt.title('Distribution Plot')

plt.tight_layout()
plt.show()

