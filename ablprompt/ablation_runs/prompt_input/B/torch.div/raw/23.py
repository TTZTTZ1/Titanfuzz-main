import torch

# Create two tensors with different shapes
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([1])

# Perform element-wise division with broadcasting and truncating rounding mode
result = torch.div(a, b, rounding_mode="trunc")

print(result)