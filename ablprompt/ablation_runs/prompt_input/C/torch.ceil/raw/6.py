import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([-1.2, -0.5, 0.3, 1.7, 2.9])

# Use torch.ceil to round up each element
result_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Result Tensor after ceil:", result_tensor)