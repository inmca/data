import numpy as np

# Create a 3D array of shape (2, 3, 4) with random integers
array_3d = np.random.randint(1, 10, size=(2, 3, 4))

# Display the array (optional)
print("3D Array: \n", array_3d)

# Display shape
print("Shape:", array_3d.shape)

# Display number of dimensions
print("Number of dimensions (ndim):", array_3d.ndim)

# Display total size (number of elements)
print("Total size (number of elements):", array_3d.size)

