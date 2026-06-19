import torch

# Create a tensor with float values
input_tensor = torch.tensor([1.2, 2.5, 3.7, -1.8])

# Use torch.ceil to round up each element
result_tensor = torch.ceil(input_tensor)

print(result_tensor)