import torch

# Create two tensors of different shapes but compatible for broadcasting
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
b = torch.tensor([2, 0.5], dtype=torch.float)

# Perform element-wise division with 'floor' rounding mode
result = torch.div(a, b, rounding_mode='floor')

print(result)