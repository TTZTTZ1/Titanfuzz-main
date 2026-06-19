import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2345, -6.7890, 2.5, -3.5])

# Round the tensor to the nearest integer
rounded_tensor = torch.round(input_tensor)

print(rounded_tensor)