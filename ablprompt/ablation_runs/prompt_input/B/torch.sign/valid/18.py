import torch

# Create a tensor with mixed values
mixed_values = torch.tensor([-5, 0, 3, -2.5, 0.0])

# Use torch.sign to get the sign of each element
signed_tensor = torch.sign(mixed_values)

print(signed_tensor)