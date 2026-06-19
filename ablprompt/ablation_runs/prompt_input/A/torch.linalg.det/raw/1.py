import torch

# Create a square matrix
matrix = torch.tensor([[4, 7], [2, 6]])

# Calculate the determinant of the matrix
determinant = torch.linalg.det(matrix)

print("The determinant of the matrix is:", determinant)