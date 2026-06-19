import torch

# Prepare input data
tensors = [torch.tensor([]), torch.tensor([1, 2, 3])]
dim = 0

# Call the API
result = torch.cat(tensors, dim)