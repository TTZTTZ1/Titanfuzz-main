import torch

# Create two random matrices
matrix1 = torch.randn(3, 4)
matrix2 = torch.randn(4, 5)

# Call the torch.mm function to multiply the matrices
result = torch.mm(matrix1, matrix2)

print(result)