import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('./assets/vgsales1.csv')

# Drop rows with missing values in key columns
df = df.dropna(subset=['Global_Sales', 'NA_Sales', 'JP_Sales', 'Genre'])

# Normalize JP_Sales for bubble size scaling
df['JP_Sales_Scaled'] = df['JP_Sales'] * 100  # adjust multiplier if needed

# -------------------------
# Bubble Chart
# -------------------------
plt.figure(figsize=(14, 8))
scatter = plt.scatter(
    x=df['Global_Sales'],
    y=df['NA_Sales'],
    s=df['JP_Sales_Scaled'],  # Bubble size
    c=pd.factorize(df['Genre'])[0],  # Color by Genre
    cmap='tab10',
    alpha=0.6,
    edgecolors='w',
    linewidth=0.5
)

# Create legend for genres
genres = df['Genre'].unique()
handles = [plt.Line2D([], [], marker='o', color='w',
                      label=genre, markerfacecolor=plt.cm.tab10(i / len(genres)),
                      markersize=10) for i, genre in enumerate(genres)]
plt.legend(handles=handles, title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.xlabel('Global Sales (millions)')
plt.ylabel('NA Sales (millions)')
plt.title('Bubble Chart of Game Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------
# 2D Density Plot
# -------------------------
plt.figure(figsize=(12, 6))
sns.kdeplot(
    x=df['Global_Sales'],
    y=df['NA_Sales'],
    cmap="Reds",
    fill=True,
    thresh=0.05,
    levels=100,
    alpha=0.7
)

plt.xlabel('Global Sales (millions)')
plt.ylabel('NA Sales (millions)')
plt.title('2D Density Plot of Game Sales')
plt.grid(True)
plt.tight_layout()
plt.show()