import torch

# Prepare valid input data
tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(2, 3)

# Call the API torch.cat
result = torch.cat((tensor1, tensor2), dim=0)