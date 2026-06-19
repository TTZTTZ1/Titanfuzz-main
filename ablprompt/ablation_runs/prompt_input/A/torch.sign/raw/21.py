import torch

# Create a tensor with some values
tensor = torch.tensor([-1.0, 0.0, 1.0])

# Use the torch.sign function to get the sign of each element in the tensor
signed_tensor = torch.sign(tensor)

print(signed_tensor)