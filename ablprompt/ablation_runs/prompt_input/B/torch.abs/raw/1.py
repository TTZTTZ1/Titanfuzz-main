import torch

# Create a random tensor with both positive and negative values
input_tensor = torch.randn(3, 4)

# Compute the absolute value using torch.abs
abs_tensor = torch.abs(input_tensor)

print(abs_tensor)