import torch

# Prepare valid input data
tensor1 = torch.tensor([])
tensor2 = torch.tensor([1, 2, 3])
tensors = [tensor1, tensor2]

# Call the API
result = torch.cat(tensors)