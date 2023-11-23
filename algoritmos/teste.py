import numpy as np

# Assuming arr is your NumPy array
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])

# Find the indices of the smallest values
min_indices = np.where(arr == np.min(arr))[0]

print("Indices of the smallest values:", min_indices)
