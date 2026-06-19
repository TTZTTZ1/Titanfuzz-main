import torch

# Create a tensor with mixed values
mixed_tensor = torch.tensor([-3, 0, 5, -2, 0])

# Use torch.sign to get the sign of each element
signed_tensor = torch.sign(mixed_tensor)

print(signed_tensor)