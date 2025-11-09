import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
titanic = sns.load_dataset('titanic')

# Count by class
class_counts = titanic['class'].value_counts()
colors = ['#ff9999', '#66b3ff', '#99ff99']

# Create pie chart
plt.pie(class_counts.values, labels=class_counts.index, colors=colors, autopct='%1.1f%%', startangle=90)

# Add title
plt.title('Pie Chart - Titanic Dataset (Class Distribution)')
plt.axis('equal')

plt.tight_layout()
plt.show()

