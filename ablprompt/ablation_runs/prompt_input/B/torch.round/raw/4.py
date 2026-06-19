import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([2.3, 4.7, -1.5, 6.2])

# Round the tensor elements to the nearest integer
rounded_tensor = torch.round(input_tensor)

print(rounded_tensor)