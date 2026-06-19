import torch

# Create a tensor with both integer and floating-point values
input_tensor = torch.tensor([-1.7, -1.2, 0.5, 1.3, 2.8])

# Apply torch.ceil to round up each element
output_tensor = torch.ceil(input_tensor)

print(output_tensor)