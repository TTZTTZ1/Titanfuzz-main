import torch

# Create a tensor with float values
input_tensor = torch.tensor([-1.2, 3.5, -0.7, 4.0])

# Use torch.ceil to round up each element
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after ceil:", output_tensor)