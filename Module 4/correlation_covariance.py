import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Sample data
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
marks_scored = np.array([35, 40, 50, 55, 60, 65, 70, 75, 80, 85])

# Calculate covariance matrix
cov_matrix = np.cov(hours_studied, marks_scored)
covariance = cov_matrix[0, 1]  # Covariance between hours_studied and marks_scored

# Calculate Pearson correlation coefficient
correlation, p_value = stats.pearsonr(hours_studied, marks_scored)

print(f"Covariance: {covariance}")
print(f"Correlation coefficient: {correlation}")

# Scatter plot
plt.scatter(hours_studied, marks_scored, color='blue', label='Data points')

# Regression line
slope, intercept, r_value, p_value, std_err = stats.linregress(hours_studied, marks_scored)
regression_line = slope * hours_studied + intercept
plt.plot(hours_studied, regression_line, color='red', label='Regression line')

plt.title('Hours Studied vs Marks Scored')
plt.xlabel('Hours Studied')
plt.ylabel('Marks Scored')
plt.legend()
plt.grid(True)
plt.show()

