import torch

# Create two tensors with different shapes but compatible for broadcasting
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([1])

# Perform element-wise division with 'floor' rounding mode
result = torch.div(a, b, rounding_mode='floor')

print(result)