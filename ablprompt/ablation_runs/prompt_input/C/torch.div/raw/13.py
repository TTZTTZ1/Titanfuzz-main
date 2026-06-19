import torch

# Create two tensors
a = torch.tensor([4.0, 8.0, 15.0, 16.0])
b = torch.tensor([2.0, 4.0, 8.0, 16.0])

# Perform element-wise division with 'floor' rounding mode
result = torch.div(a, b, rounding_mode='floor')

print(result)