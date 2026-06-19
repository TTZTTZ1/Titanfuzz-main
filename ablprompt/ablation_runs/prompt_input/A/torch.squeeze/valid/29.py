import torch

# Create a tensor with an extra singleton dimension
tensor = torch.randn(1, 2, 3)

# Squeeze the singleton dimension
squeezed_tensor = torch.squeeze(tensor)

print(squeezed_tensor)