import torch

# Create two tensors
a = torch.tensor([[10, 20], [30, 40]], dtype=torch.float32)
b = torch.tensor([[2, 2], [5, 8]], dtype=torch.float32)

# Perform element-wise division with rounding mode 'floor'
result = torch.div(a, b, rounding_mode='floor')

print(result)