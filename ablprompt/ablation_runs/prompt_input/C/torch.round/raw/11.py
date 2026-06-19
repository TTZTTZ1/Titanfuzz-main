import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([2.5, 3.4, 4.6, -1.7])

# Round the tensor elements to the nearest integer
rounded_tensor = torch.round(input_tensor)

print("Original Tensor:", input_tensor)
print("Rounded Tensor:", rounded_tensor)