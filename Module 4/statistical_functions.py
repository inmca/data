import statistics

# Function to calculate the mean
def calculate_mean(data):
    return sum(data) / len(data)

# Function to calculate the median
def calculate_median(data):
    return statistics.median(data)

# Function to calculate the mode
def calculate_mode(data):
    return statistics.mode(data)

# Function to calculate the variance
def calculate_variance(data):
    return statistics.variance(data)

# Function to calculate the standard deviation
def calculate_standard_deviation(data):
    return statistics.stdev(data)

# Example usage
data = [10, 20, 20, 30, 40, 50]

mean = calculate_mean(data)
median = calculate_median(data)
mode = calculate_mode(data)
variance = calculate_variance(data)
std_deviation = calculate_standard_deviation(data)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)

