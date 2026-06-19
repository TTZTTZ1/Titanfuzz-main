import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2345, -2.7890, 3.1415, -4.6789])

# Round the tensor elements to the nearest integer
rounded_tensor = torch.round(input_tensor)

print("Original Tensor:", input_tensor)
print("Rounded Tensor:", rounded_tensor)