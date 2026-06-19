import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Define scalar minimum and maximum values
min_value = -0.5
max_value = 0.5

# Clamp the tensor using scalar min and max values
clamped_tensor = torch.clamp(input_tensor, min=min_value, max=max_value)

print(clamped_tensor)