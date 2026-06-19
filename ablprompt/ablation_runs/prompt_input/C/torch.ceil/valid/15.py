import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2, 3.5, -0.7, 4.8])

# Apply torch.ceil to round up each element
result_tensor = torch.ceil(input_tensor)

print(result_tensor)