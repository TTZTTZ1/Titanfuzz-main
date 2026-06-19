import torch

# Create two tensors with different shapes
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([5, 6], dtype=torch.float32)

# Perform element-wise division with broadcasting and rounding mode 'floor'
result = torch.div(a, b, rounding_mode='floor')

print(result)