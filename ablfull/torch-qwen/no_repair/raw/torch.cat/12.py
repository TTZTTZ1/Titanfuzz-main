import torch

# Prepare valid input data
tensor1 = torch.tensor([])
tensor2 = torch.tensor([1, 2, 3])
dim = 0

# Call the API
result = torch.cat((tensor1, tensor2), dim=dim)