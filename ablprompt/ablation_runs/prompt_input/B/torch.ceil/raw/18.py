import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2, 3.7, -2.5, 0.0])

# Apply torch.ceil to round up each element
output_tensor = torch.ceil(input_tensor)

print(output_tensor)