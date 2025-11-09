import math

# Set of positive numbers
numbers = [1, 2, 5, 10, 20, 100]

# Using log(), log10(), and log2()
log_values = {
    "log(x) (Natural Log)": [math.log(x) for x in numbers],
    "log10(x)": [math.log10(x) for x in numbers],
    "log2(x)": [math.log2(x) for x in numbers],
}

# Display results
for label, values in log_values.items():
    print(f"{label}: {values}")

