import numpy as np

# Create a 1D array of 10 random integers between 1 and 100 (inclusive)
random_array = np.random.randint(1, 101, size=10)

# Calculate maximum
max_value = np.max(random_array)

# Calculate minimum
min_value = np.min(random_array)

# Calculate mean
mean_value = np.mean(random_array)

# Calculate standard deviation
std_deviation = np.std(random_array)

# Display results
print("Random Array:", random_array)
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
print(f"Mean: {mean_value:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")

