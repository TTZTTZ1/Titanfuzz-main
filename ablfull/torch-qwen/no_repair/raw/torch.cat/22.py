import torch

# Prepare input data
tensors = [torch.tensor([1, 2, 3]), torch.tensor([4, 5])]
dim = 0

# Call the API
result = torch.cat(tensors, dim=dim)