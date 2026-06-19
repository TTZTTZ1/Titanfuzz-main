import torch

# Create a tensor with both positive, negative, and zero values
input_tensor = torch.tensor([-2.5, 0.0, 3.14])

# Use torch.sign to get the sign of each element
signed_tensor = torch.sign(input_tensor)

print(signed_tensor)