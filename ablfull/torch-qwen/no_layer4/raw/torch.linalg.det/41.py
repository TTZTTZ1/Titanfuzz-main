import torch

# Generate input data
A = torch.randn(2, 2)

# Call the API
result = torch.linalg.det(A)