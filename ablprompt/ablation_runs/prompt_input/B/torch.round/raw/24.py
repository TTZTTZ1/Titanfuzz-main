import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Round the tensor to the nearest integer
rounded_tensor = torch.round(input_tensor)

print(rounded_tensor)