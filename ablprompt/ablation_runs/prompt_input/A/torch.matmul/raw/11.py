import torch

# Create two random matrices
matrix1 = torch.randn(3, 4)
matrix2 = torch.randn(4, 5)

# Call the torch.matmul function
result = torch.matmul(matrix1, matrix2)

# Print the result
print(result)