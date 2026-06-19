import torch

# Create two tensors
a = torch.tensor([[4.0, -3.0], [2.0, 5.0]])
b = torch.tensor([[[1.0], [-1.0]], [[2.0], [0.5]]])

# Perform element-wise division with 'floor' rounding mode
result = torch.div(a, b, rounding_mode='floor')

print(result)