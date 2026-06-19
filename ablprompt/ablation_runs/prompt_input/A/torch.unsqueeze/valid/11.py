import torch

# Create a tensor
tensor = torch.randn(3, 4)

# Use torch.unsqueeze to add an extra dimension at index 0
unsqueezed_tensor = torch.unsqueeze(tensor, 0)

print("Original Tensor:", tensor)
print("Unsqueezed Tensor:", unsqueezed_tensor)