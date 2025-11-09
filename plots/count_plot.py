import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
df = pd.read_csv('./assets/titanic_train.csv')

# Create count plot
sns.countplot(x='Pclass', data=df)

# Add labels and title
plt.xlabel('Class')
plt.ylabel('Count')
plt.title('Count Plot')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

