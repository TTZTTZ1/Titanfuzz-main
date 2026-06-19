import torch

# Create random matrices
input_matrix = torch.randn(5, 3)
mat2_matrix = torch.randn(3, 7)

# Perform matrix multiplication
result_matrix = torch.mm(input_matrix, mat2_matrix)

print(result_matrix)