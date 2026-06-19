import torch

# Create two tensors
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[2.0, 2.0], [2.0, 2.0]])

# Perform element-wise division with rounding mode 'trunc'
result = torch.div(a, b, rounding_mode='trunc')

print(result)