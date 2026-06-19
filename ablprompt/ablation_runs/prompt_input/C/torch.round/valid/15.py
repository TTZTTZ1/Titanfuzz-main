import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.234, -5.678, 9.012])

# Round the tensor to the nearest integer
rounded_tensor = torch.round(input_tensor)

print("Original Tensor:", input_tensor)
print("Rounded Tensor:", rounded_tensor)