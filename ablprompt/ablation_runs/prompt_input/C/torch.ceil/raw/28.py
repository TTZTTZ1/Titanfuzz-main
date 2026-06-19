import torch

# Create a tensor with float values
input_tensor = torch.tensor([1.2, -3.7, 4.5, -6.8])

# Apply torch.ceil to round up each element
result_tensor = torch.ceil(input_tensor)

print(result_tensor)