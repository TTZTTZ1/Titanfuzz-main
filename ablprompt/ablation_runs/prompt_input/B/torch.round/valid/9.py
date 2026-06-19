import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2345, -2.7890, 3.4567])

# Round the tensor elements to the nearest integer
rounded_tensor = torch.round(input_tensor)

print(rounded_tensor)