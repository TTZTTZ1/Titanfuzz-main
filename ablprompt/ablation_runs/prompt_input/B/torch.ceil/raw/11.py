import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([-1.2, -0.8, 0.5, 1.3, 2.7])

# Use torch.ceil to round up each element
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)