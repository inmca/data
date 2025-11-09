import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv('./assets/titanic_train.csv')

# Count by class (Pclass column)
class_counts = df['Pclass'].value_counts().sort_index()
colors = ['#ff9999', '#66b3ff', '#99ff99']

# Create pie chart
plt.pie(class_counts.values, labels=[f'Class {i}' for i in class_counts.index], colors=colors, autopct='%1.1f%%', startangle=90)

# Add title
plt.title('Pie Chart')
plt.axis('equal')

plt.tight_layout()
plt.show()

