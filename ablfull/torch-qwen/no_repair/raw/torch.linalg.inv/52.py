import torch

# Generate a valid input tensor
A = torch.randn(4, 4)

# Call the API
result = torch.linalg.inv(A)