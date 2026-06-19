import torch

# Generate a random 3x3 matrix to ensure it's invertible
input_matrix = torch.randn(3, 3)

# Ensure the matrix is invertible by checking its determinant
while torch.abs(torch.det(input_matrix)) < 1e-6:
    input_matrix = torch.randn(3, 3)

# Call the API
result = torch.linalg.inv(input_matrix)