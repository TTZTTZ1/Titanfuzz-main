import torch

# Create a tensor with both integer and float values
input_tensor = torch.tensor([-1.2, -0.5, 0.3, 1.7, 2])

# Apply torch.ceil to round up each element
output_tensor = torch.ceil(input_tensor)

print(output_tensor)