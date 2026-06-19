import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Define min and max values
min_value = -0.5
max_value = 0.5

# Clamp the tensor
clamped_tensor = torch.clamp(input_tensor, min=min_value, max=max_value)

print(clamped_tensor)