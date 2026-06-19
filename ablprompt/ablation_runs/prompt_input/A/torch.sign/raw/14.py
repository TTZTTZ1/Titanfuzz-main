import torch

# Create a tensor with both positive and negative values
tensor = torch.tensor([-1.0, 0.0, 1.0])

# Use torch.sign to get the sign of each element in the tensor
signed_tensor = torch.sign(tensor)

print(signed_tensor)