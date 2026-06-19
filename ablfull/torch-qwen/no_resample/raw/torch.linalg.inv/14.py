import torch

# Generate a random square matrix of size 3x3 with float type
A = torch.randn(3, 3)

# Call the torch.linalg.inv function
result = torch.linalg.inv(A)