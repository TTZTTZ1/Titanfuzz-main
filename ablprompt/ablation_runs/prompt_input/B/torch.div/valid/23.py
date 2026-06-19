import torch

# Create two tensors with different shapes
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([0.5])

# Perform element-wise division using torch.div with 'floor' rounding mode
result = torch.div(a, b, rounding_mode='floor')

print(result)