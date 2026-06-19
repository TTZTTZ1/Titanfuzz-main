import torch

# Create a tensor with both positive, negative, and zero values
input_tensor = torch.tensor([-5, 0, 5], dtype=torch.float32)

# Use torch.sign to get the sign of each element in the tensor
signed_tensor = torch.sign(input_tensor)

print(signed_tensor)