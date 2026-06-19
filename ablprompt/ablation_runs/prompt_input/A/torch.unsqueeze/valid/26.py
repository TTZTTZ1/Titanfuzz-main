import torch

# Create a tensor
tensor = torch.randn(3, 4)

# Use torch.unsqueeze to add a new dimension at index 0
unsqueezed_tensor = torch.unsqueeze(tensor, 0)

print("Original Tensor shape:", tensor.shape)
print("Unsqueezed Tensor shape:", unsqueezed_tensor.shape)