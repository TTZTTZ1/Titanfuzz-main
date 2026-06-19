import torch

# Create a sample tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0, 2.0])

# Use torch.clamp to clamp values between -0.5 and 1.5
clamped_tensor = torch.clamp(input_tensor, min=-0.5, max=1.5)

print(clamped_tensor)