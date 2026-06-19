import torch

# Generate input data
A = torch.randn(3, 3, dtype=torch.float)

# Call the API
result = torch.linalg.det(A)