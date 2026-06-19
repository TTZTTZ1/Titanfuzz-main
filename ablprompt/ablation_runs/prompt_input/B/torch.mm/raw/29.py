import torch

# Create two random matrices
input_matrix = torch.randn(3, 4)
mat2_matrix = torch.randn(4, 5)

# Perform matrix multiplication
output_matrix = torch.mm(input_matrix, mat2_matrix)

print(output_matrix)