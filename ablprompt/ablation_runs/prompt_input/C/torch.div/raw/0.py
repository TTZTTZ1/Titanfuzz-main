import torch

# Create two tensors of different shapes but compatible for broadcasting
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
b = torch.tensor([1, 2])

# Perform element-wise division with truncating rounding mode
result = torch.div(a, b, rounding_mode="trunc")

print(result)