import torch

# Prepare valid input data
args = (torch.tensor([1, 2, 3], dtype=torch.int),)

# Call the API
result = torch.QInt32Storage(*args)