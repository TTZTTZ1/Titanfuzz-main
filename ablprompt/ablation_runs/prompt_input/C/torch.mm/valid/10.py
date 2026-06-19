import torch

# Create two random matrices
matrix1 = torch.randn(3, 5)
matrix2 = torch.randn(5, 7)

# Perform matrix multiplication
result = torch.mm(matrix1, matrix2)

print(result)