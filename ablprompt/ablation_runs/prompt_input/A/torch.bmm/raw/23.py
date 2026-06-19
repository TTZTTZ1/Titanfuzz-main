import torch

# Create two 3x3 matrices
matrix1 = torch.randn(3, 3)
matrix2 = torch.randn(3, 3)

# Perform batch matrix multiplication using torch.bmm
result = torch.bmm(matrix1.unsqueeze(0), matrix2.unsqueeze(0))

print(result)