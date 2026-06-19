import torch

# Create a tensor with mixed values
input_tensor = torch.tensor([-3.5, 0.0, 2.1, -4.8])

# Use torch.sign to get the sign of each element
signed_tensor = torch.sign(input_tensor)

print(signed_tensor)