import torch

# Create a random tensor with shape (3, 4)
input_tensor = torch.randn(3, 4)

# Insert a new dimension at index 1
unsqueezed_tensor = torch.unsqueeze(input_tensor, dim=1)

print("Original Tensor Shape:", input_tensor.shape)
print("Unsqueezed Tensor Shape:", unsqueezed_tensor.shape)