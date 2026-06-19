import torch

# Create two tensors
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
b = torch.tensor([[1.0, 2.0], [2.0, 2.0]], dtype=torch.float32)

# Perform element-wise division with rounding mode 'floor'
result = torch.div(a, b, rounding_mode='floor')

print(result)