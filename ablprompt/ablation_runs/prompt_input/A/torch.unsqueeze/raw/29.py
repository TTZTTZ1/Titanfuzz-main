import torch

# Create a tensor
tensor = torch.randn(3, 4)

# Use torch.unsqueeze to add a new dimension at index 1
unsqueezed_tensor = torch.unsqueeze(tensor, 1)

print(unsqueezed_tensor.shape)