import math

# Function to calculate square root
def calculate_square_root(number):
    return math.sqrt(number)

# Function to calculate exponential value (e^x)
def calculate_exponential(number):
    return math.exp(number)

# Function to calculate power of a number (x^y)
def calculate_power(base, exponent):
    return math.pow(base, exponent)

# Example usage
num = 16  # Number for square root and exponential example
base = 2  # Base for power calculation
exponent = 3  # Exponent for power calculation

# Calculating square root
sqrt_result = calculate_square_root(num)

# Calculating exponential
exp_result = calculate_exponential(num)

# Calculating power
pow_result = calculate_power(base, exponent)

# Display results
print(f"Square root of {num}: {sqrt_result}")
print(f"Exponential of {num} (e^{num}): {exp_result}")
print(f"{base} raised to the power of {exponent} ({base}^{exponent}): {pow_result}")

