import torch

# Create some tensors
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

# Use torch.stack to stack them along a new dimension
stacked_tensors = torch.stack((tensor1, tensor2))

print(stacked_tensors)