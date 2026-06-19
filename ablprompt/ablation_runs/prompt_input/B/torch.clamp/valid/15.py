import torch

# Create a sample tensor
input_tensor = torch.tensor([-1.5, 0.3, 2.7, -0.8])

# Clamp the tensor values between -1 and 1
clamped_tensor = torch.clamp(input_tensor, min=-1, max=1)

print(clamped_tensor)