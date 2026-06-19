import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Insert a new dimension at index 0
unsqueezed_tensor = torch.unsqueeze(input_tensor, 0)

print("Original Tensor:", input_tensor)
print("Unsqueezed Tensor:", unsqueezed_tensor)
print("Shape of Original Tensor:", input_tensor.shape)
print("Shape of Unsqueezed Tensor:", unsqueezed_tensor.shape)