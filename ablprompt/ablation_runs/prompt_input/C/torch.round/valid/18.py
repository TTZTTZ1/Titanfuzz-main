import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.tensor([1.2345, -6.7890, 2.3456, -7.8901], dtype=torch.float32)

# Round the tensor elements to the nearest integer
rounded_tensor = torch.round(input_tensor)

print("Original Tensor:", input_tensor)
print("Rounded Tensor:", rounded_tensor)