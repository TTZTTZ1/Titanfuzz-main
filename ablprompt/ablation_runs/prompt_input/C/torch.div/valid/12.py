import torch

# Create two tensors of different shapes but compatible for broadcasting
a = torch.tensor([[4.0, 5.0], [6.0, 7.0]])
b = torch.tensor([2.0])

# Perform element-wise division with truncating rounding mode
result = torch.div(a, b, rounding_mode="trunc")

print(result)