import numpy as np

# Example 2D array: rows represent products, columns represent regions
sales = np.array([
    [120, 150, 100],  # Product 1 sales in Region 1, 2, 3
    [80,  90,  60],   # Product 2 sales
    [200, 210, 180],  # Product 3 sales
    [150, 130, 170]   # Product 4 sales
])

# Total sales per product (sum across columns)
total_sales_per_product = np.sum(sales, axis=1)

# Total sales per region (sum across rows)
total_sales_per_region = np.sum(sales, axis=0)

# Display results
print("Total sales per product:")
for i, total in enumerate(total_sales_per_product, start=1):
    print(f"Product {i}: {total}")

print("\nTotal sales per region:")
for j, total in enumerate(total_sales_per_region, start=1):
    print(f"Region {j}: {total}")

