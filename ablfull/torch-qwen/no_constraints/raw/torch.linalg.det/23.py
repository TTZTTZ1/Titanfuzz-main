import torch

# Task 2: Generate input data
matrix = torch.tensor([[4., 7.], [2., 6.]])  # Valid input as it is a square matrix

# Task 3: Call the API
result = torch.linalg.det(matrix)
print(result)