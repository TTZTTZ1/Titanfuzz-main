import torch

# Generate input data
A = torch.randn(4, 4, dtype=torch.float)

# Call the API
result = torch.linalg.det(A)