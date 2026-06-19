import torch

# Create a tensor with both integer and float values
input_tensor = torch.tensor([-2.5, -1.3, 0.7, 1.9], dtype=torch.float)

# Apply torch.ceil to round up each element
result_tensor = torch.ceil(input_tensor)

print(result_tensor)