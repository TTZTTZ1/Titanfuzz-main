import torch

# Create a tensor with mixed values
mixed_values = torch.tensor([-2, 0, 3, -4, 5])

# Use torch.sign to get the sign of each element
signed_tensor = torch.sign(mixed_values)

print(signed_tensor)