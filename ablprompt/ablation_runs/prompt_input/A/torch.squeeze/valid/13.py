import torch

# Create a tensor with an extra singleton dimension
tensor = torch.randn(1, 2, 3, 1)

# Squeeze the singleton dimensions
squeezed_tensor = torch.squeeze(tensor)

print(squeezed_tensor)