import torch

# Create two tensors of different shapes
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([0.5])

# Perform element-wise division with broadcasting
result = torch.div(a, b, rounding_mode='floor')

print(result)