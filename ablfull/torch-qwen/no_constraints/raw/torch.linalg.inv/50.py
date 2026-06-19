import torch

# Task 2: Generate input data
matrix = torch.tensor([[4., 7.], [2., 6.]])  # Example square matrix, invertible

# Task 3: Call the API
inverse_matrix = torch.linalg.inv(matrix)
print(inverse_matrix)