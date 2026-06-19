import torch

# Create a tensor with various values including positive, negative, and zero
input_tensor = torch.tensor([-5, 0, 3, -2, 0])

# Use torch.sign to get the sign of each element in the tensor
signed_tensor = torch.sign(input_tensor)

print(signed_tensor)