import torch

# Create a 2x2 tensor
matrix = torch.tensor([[4.0, 7.0], [2.0, 6.0]])

# Calculate the determinant of the matrix
determinant = torch.linalg.det(matrix)

print("The determinant of the matrix is:", determinant)