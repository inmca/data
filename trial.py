import matplotlib.pyplot as plt
import pandas as pd

# Create a new dataset
data = {
    'Fruits': ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes'],
    'Quantity': [15, 30, 20, 25, 10]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create bar plot
plt.figure(figsize=(8, 5))
plt.bar(df['Fruits'], df['Quantity'], color='skyblue')

# Add labels and title
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title('Fruit Quantities')

# Show plot
plt.show()
