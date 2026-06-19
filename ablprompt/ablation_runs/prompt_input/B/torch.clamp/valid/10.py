import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Clamp the tensor between -1 and 1
clamped_tensor = torch.clamp(input_tensor, min=-1, max=1)

print(clamped_tensor)