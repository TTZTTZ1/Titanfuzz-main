import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.tensor([1.234, -2.789, 3.567, -4.444], dtype=torch.float32)

# Round the tensor elements to the nearest integer
rounded_tensor = torch.round(input_tensor)

print("Original Tensor:", input_tensor)
print("Rounded Tensor:", rounded_tensor)