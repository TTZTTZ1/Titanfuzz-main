import torch

# Create two random matrices
matrix1 = torch.randn(2, 3)
matrix2 = torch.randn(3, 4)

# Call the torch.matmul function
result = torch.matmul(matrix1, matrix2)

print(result)