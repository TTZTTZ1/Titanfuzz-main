import torch

# Prepare valid input data
A = torch.randn(2, 3, 3, dtype=torch.float)

# Call the API
result = torch.linalg.det(A)