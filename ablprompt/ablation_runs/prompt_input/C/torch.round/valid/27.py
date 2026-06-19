import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([2.5, -3.7, 4.2, -5.8])

# Round the tensor elements to the nearest integer
rounded_tensor = torch.round(input_tensor)

print("Original Tensor:", input_tensor)
print("Rounded Tensor:", rounded_tensor)