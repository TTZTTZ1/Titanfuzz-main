import torch

# Create two tensors with different shapes but compatible dimensions for broadcasting
a = torch.tensor([[4.0, 8.0], [16.0, 32.0]])
b = torch.tensor([2.0])

# Perform element-wise division with truncating rounding mode
result = torch.div(a, b, rounding_mode="trunc")

print(result)