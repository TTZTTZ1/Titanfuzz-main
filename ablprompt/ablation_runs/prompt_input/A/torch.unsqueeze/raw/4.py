import torch

# Create a tensor
tensor = torch.randn(3, 4)

# Use torch.unsqueeze to add an extra dimension at index 1
unsqueezed_tensor = torch.unsqueeze(tensor, 1)

print("Original Tensor:", tensor.shape)
print("Unsqueezed Tensor:", unsqueezed_tensor.shape)