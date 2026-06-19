import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.tensor([1.2345, -2.7890, 3.4567, -4.1234], dtype=torch.float32)

# Round the tensor elements to the nearest integer
rounded_tensor = torch.round(input_tensor)

print("Original Tensor:", input_tensor)
print("Rounded Tensor:", rounded_tensor)