import torch

# Create two tensors with different shapes
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([1, 2])

# Perform element-wise division with broadcasting and 'floor' rounding mode
result = torch.div(a, b, rounding_mode='floor')

print(result)