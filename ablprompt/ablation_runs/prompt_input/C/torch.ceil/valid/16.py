import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([-1.2, 3.5, -4.8, 2.0])

# Apply torch.ceil to round up each element
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after ceil:", output_tensor)