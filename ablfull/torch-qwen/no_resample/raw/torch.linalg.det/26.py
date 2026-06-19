import torch

# Generate input data
A = torch.randn(4, 4)

# Call the API
result = torch.linalg.det(A)