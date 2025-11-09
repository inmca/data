import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
titanic = sns.load_dataset('titanic')

# Create count plot
sns.countplot(x='class', data=titanic)

# Add labels and title
plt.xlabel('Class')
plt.ylabel('Count')
plt.title('Count Plot - Titanic Dataset')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

