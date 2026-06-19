import torch

# Create two tensors with different shapes but compatible dimensions
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
b = torch.tensor([1, 2], dtype=torch.float)

# Perform element-wise division with truncating rounding mode
result = torch.div(a, b, rounding_mode="trunc")

print(result)