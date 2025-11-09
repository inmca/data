import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('./assets/StudentsPerformance.csv')
print("All entries")
print(df)
print("Duplicates")
print(df.duplicated())
print("After dropping duplicates")
print(df.drop_duplicates())