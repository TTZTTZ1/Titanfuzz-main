import torch

# Task 2: Generate input data
matrix = torch.tensor([[4., 7.], [2., 6.]])

# Task 3: Call the API
result = torch.linalg.det(matrix)
print(result)