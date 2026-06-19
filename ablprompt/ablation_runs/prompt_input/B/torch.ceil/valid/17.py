import torch

# Create a tensor with both positive and negative floating-point numbers
input_tensor = torch.tensor([-2.3, -1.7, 0.5, 1.2, 2.8])

# Use torch.ceil to round up each element
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after ceil:", output_tensor)