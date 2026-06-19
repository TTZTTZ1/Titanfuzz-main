import torch

# Create a tensor with some values
tensor = torch.tensor([-1.0, 2.5, -3.0, 4.5])

# Use torch.clamp to clamp the values between -2 and 3
clamped_tensor = torch.clamp(tensor, min=-2, max=3)

print(clamped_tensor)