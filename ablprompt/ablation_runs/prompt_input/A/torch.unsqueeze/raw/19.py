import torch

# Create a tensor
tensor = torch.randn(3, 4)

# Use torch.unsqueeze to add an extra dimension at index 1
unsqueezed_tensor = torch.unsqueeze(tensor, 1)

print(unsqueezed_tensor.shape)  # Output should be torch.Size([3, 1, 4])