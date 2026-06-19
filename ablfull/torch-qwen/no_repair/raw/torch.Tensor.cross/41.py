import torch

# Prepare valid input data
a = torch.tensor([1, 0, 0])
b = torch.tensor([0, 1, 0])

# Call the API
result = a.cross(b)