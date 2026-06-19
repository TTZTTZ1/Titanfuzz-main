import torch

# Prepare valid input data
a = torch.randn(4, 3)

# Call the API
result = torch.transpose(a, 0, 1)