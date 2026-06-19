import torch

# Create a list of tensors
tensors = [torch.randn(3), torch.randn(3), torch.randn(3)]

# Stack them along a new dimension
stacked_tensor = torch.stack(tensors, dim=0)

print(stacked_tensor)