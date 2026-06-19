import torch

# Create two tensors with different shapes
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([1.0])

# Perform element-wise division with broadcasting and rounding mode 'floor'
result = torch.div(a, b, rounding_mode='floor')

print(result)