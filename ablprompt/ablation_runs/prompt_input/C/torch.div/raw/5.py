import torch

# Create two tensors with different shapes but compatible for broadcasting
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([1, 2], dtype=torch.float32)

# Perform element-wise division using torch.div
result = torch.div(a, b, rounding_mode='floor')

print(result)