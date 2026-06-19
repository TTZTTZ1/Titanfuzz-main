import torch

# Prepare valid input data
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])

# Call the API
result = torch.cat((tensor1, tensor2), dim=0)