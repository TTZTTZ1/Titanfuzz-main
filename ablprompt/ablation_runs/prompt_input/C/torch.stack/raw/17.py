import torch

# Create a list of tensors with the same shape
tensors = [torch.randn(2, 3), torch.randn(2, 3)]

# Stack the tensors along a new dimension
stacked_tensor = torch.stack(tensors, dim=0)

print(stacked_tensor)