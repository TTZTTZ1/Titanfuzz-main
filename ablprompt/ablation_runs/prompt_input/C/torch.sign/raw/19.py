import torch

# Create a tensor with mixed values
mixed_tensor = torch.tensor([-5, 0, 3, -2.5])

# Use torch.sign to get the sign of each element
signed_tensor = torch.sign(mixed_tensor)

print(signed_tensor)