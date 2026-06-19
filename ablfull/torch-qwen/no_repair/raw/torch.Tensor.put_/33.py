import torch

# Prepare valid input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([3, 4, 5])

# Call the API
result = torch.Tensor().put_(index, source)