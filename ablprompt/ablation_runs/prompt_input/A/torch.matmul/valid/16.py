import torch

# Create two random matrices
matrix1 = torch.randn(2, 3)
matrix2 = torch.randn(3, 4)

# Perform matrix multiplication using torch.matmul
result = torch.matmul(matrix1, matrix2)

print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Result of matrix multiplication:")
print(result)