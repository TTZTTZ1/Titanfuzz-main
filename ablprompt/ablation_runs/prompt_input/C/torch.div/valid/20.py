import torch

# Create two tensors
a = torch.tensor([4.0, -3.0, 5.0], dtype=torch.float32)
b = torch.tensor([2.0, 2.0, 2.0], dtype=torch.float32)

# Perform element-wise division with rounding mode 'trunc'
result = torch.div(a, b, rounding_mode='trunc')

print(result)