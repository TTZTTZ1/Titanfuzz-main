import torch

# Create two tensors with different shapes but compatible for broadcasting
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([1, 2])

# Perform element-wise division with truncation rounding mode
result = torch.div(a, b, rounding_mode="trunc")

print(result)