import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Define min and max values
min_value = -1.0
max_value = 1.0

# Clamp the tensor
clamped_tensor = torch.clamp(input_tensor, min=min_value, max=max_value)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)