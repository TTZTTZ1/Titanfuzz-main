import torch

# Create a tensor
tensor = torch.randn(3, 4)

# Use torch.unsqueeze to add an additional dimension at index 0
unsqueezed_tensor = torch.unsqueeze(tensor, 0)

print("Original Tensor Shape:", tensor.shape)
print("Unsqueezed Tensor Shape:", unsqueezed_tensor.shape)