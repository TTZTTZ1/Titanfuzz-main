import torch

# Prepare valid input data
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

# Call the API torch.cat
result = torch.cat((tensor1, tensor2))