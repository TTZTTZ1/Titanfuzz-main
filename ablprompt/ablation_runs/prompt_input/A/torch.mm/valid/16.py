import torch

# Create two 2x3 matrices
matrix1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
matrix2 = torch.tensor([[7, 8], [9, 10], [11, 12]])

# Perform matrix multiplication using torch.mm
result = torch.mm(matrix1, matrix2)

print(result)