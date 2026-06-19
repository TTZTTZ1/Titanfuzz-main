import torch

# Generate input data
A = torch.randn(3, 3)

# Call the API
result = torch.linalg.inv(A)