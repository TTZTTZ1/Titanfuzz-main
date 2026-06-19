import torch

# Prepare valid input data
A = torch.randn(3, 3, dtype=torch.float)

# Call the target API
result = torch.linalg.inv_ex(A)