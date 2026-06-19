import torch

# Prepare valid input data
A = torch.randn(3, 3)

# Call the API
result = torch.linalg.det(A)