import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.rand(4, 4) * 10 - 5  # Values between -5 and 5

# Round the tensor to the nearest integer
rounded_tensor = torch.round(input_tensor)

print("Original Tensor:")
print(input_tensor)
print("Rounded Tensor:")
print(rounded_tensor)