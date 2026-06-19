import torch

# Prepare input data
A = torch.randn(3, 3, dtype=torch.float64)

# Call the API
result = torch.linalg.inv_ex(A)