import torch

# Create a sample tensor
x = torch.tensor([-1.0, 0.5, 2.0, 3.5])

# Clamp the tensor values between -0.5 and 2.0
clamped_x = torch.clamp(x, min=-0.5, max=2.0)

print(clamped_x)