import torch

# Generate a random 3x3 matrix with values between -10 and 10
input_matrix = torch.rand(3, 3) * 20 - 10

# Calculate the determinant of the matrix
determinant = torch.linalg.det(input_matrix)