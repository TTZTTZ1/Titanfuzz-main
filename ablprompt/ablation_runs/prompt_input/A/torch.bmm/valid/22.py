import torch

# Create two random matrices for batch matrix multiplication
batch_size = 2
matrix1 = torch.randn(batch_size, 3, 4)
matrix2 = torch.randn(batch_size, 4, 5)

# Perform batch matrix multiplication using torch.bmm
result = torch.bmm(matrix1, matrix2)

print(result)