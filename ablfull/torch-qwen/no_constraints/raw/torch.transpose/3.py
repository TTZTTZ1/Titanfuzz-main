import torch

# Prepare valid input data
x = torch.randn(4, 3)

# Call the API
result = torch.transpose(x, 0, 1)