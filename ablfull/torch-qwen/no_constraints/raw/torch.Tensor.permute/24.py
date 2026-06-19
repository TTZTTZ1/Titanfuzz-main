import torch

# Prepare valid input data
data = torch.randn(2, 3, 4)

# Call the API
result = data.permute(2, 0, 1)