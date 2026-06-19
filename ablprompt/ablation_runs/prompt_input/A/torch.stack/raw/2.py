import torch

# Create a list of tensors
tensors = [torch.randn(3), torch.randn(3), torch.randn(3)]

# Use torch.stack to stack them along a new dimension
stacked_tensor = torch.stack(tensors)

print(stacked_tensor)