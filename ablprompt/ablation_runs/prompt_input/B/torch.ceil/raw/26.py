import torch

# Create a tensor with both integer and float values
input_tensor = torch.tensor([-1.2, -0.7, 0.3, 1.5])

# Apply torch.ceil to round up each element
result_tensor = torch.ceil(input_tensor)

print(result_tensor)