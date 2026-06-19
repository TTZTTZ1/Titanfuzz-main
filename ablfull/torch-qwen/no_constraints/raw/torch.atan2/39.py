import torch

# Prepare valid input data
y = torch.tensor([1.0])
x = torch.tensor([1.0])

# Call the API
result = torch.atan2(y, x)