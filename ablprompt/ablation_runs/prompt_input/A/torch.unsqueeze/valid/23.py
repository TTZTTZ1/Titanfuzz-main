import torch

# Create a tensor
tensor = torch.randn(3, 4)

# Use torch.unsqueeze to add a dimension at index 1
unsqueezed_tensor = torch.unsqueeze(tensor, 1)

print("Original Tensor:", tensor)
print("Unsqueezed Tensor:", unsqueezed_tensor)