import torch

# Create a tensor with mixed values
input_tensor = torch.tensor([-5, 0, 3.14, -2.718])

# Use torch.sign to get the sign of each element
signed_tensor = torch.sign(input_tensor)

print(signed_tensor)