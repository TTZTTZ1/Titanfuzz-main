import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Insert a new dimension at index 1
unsqueezed_tensor = torch.unsqueeze(input_tensor, 1)

print("Original Tensor:", input_tensor.shape)
print("Unsqueezed Tensor:", unsqueezed_tensor.shape)