import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([-1.2, 3.5, -4.8, 5.0], dtype=torch.float)

# Use torch.ceil to round up each element to the nearest integer
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)