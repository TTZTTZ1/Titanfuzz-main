import torch

# Prepare input data
A = torch.randn(2, 2, dtype=torch.float)

# Call the API
result = torch.linalg.inv_ex(A)