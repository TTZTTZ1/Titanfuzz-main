import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2345, -2.7890, 3.1415, -4.6789])

# Round the tensor to 2 decimal places
rounded_tensor = torch.round(input_tensor, decimals=2)

print(rounded_tensor)