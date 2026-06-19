import torch

# Create two tensors with different shapes but compatible for broadcasting
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
b = torch.tensor([0.5, 1.0], dtype=torch.float)

# Perform element-wise division using torch.div with 'floor' rounding mode
result = torch.div(a, b, rounding_mode='floor')

print(result)