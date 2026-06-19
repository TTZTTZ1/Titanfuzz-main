import torch

# Task 2: Generate input data - a square matrix with non-zero determinant
input_matrix = torch.tensor([[4.0, 7.0], [2.0, 6.0]])

# Task 3: Call the API torch.linalg.inv
result = torch.linalg.inv(input_matrix)
print(result)