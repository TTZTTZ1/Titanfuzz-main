import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.randn(3, 4) * 10  # Random tensor between -10 and 10

# Round the tensor to the nearest integer
rounded_tensor = torch.round(input_tensor)

print("Original Tensor:")
print(input_tensor)
print("Rounded Tensor:")
print(rounded_tensor)