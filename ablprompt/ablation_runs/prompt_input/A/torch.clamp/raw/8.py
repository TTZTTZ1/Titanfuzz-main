import torch

# Create a tensor
tensor = torch.tensor([-1.0, 2.0, 3.0])

# Clamp the tensor values between -1 and 2
clamped_tensor = torch.clamp(tensor, min=-1, max=2)

print(clamped_tensor)