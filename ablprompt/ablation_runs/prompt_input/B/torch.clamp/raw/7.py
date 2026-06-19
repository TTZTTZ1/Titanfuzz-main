import torch

# Create a tensor with random values
input_tensor = torch.randn(3, 4)

# Define min and max values
min_val = -0.5
max_val = 0.5

# Clamp the tensor values between min and max
clamped_tensor = torch.clamp(input_tensor, min=min_val, max=max_val)

print(clamped_tensor)