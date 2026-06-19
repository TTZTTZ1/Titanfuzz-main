import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.randn(3, 4)

# Round the tensor elements to the nearest integer
rounded_tensor = torch.round(input_tensor)

print("Original Tensor:", input_tensor)
print("Rounded Tensor:", rounded_tensor)