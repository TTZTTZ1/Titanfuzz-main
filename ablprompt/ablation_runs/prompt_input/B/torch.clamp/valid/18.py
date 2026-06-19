import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Clamp the tensor values between -0.5 and 0.5
clamped_tensor = torch.clamp(input_tensor, min=-0.5, max=0.5)

print(clamped_tensor)