import torch

# Create two random matrices
input_matrix = torch.randn(5, 3)
mat2_matrix = torch.randn(3, 4)

# Perform matrix multiplication
result = torch.mm(input_matrix, mat2_matrix)

print(result)