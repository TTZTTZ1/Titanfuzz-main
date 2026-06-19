import torch

# Create two tensors
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[0.5, 1], [1.5, 2]], dtype=torch.float32)

# Perform element-wise division with rounding mode 'trunc'
result = torch.div(a, b, rounding_mode='trunc')

print(result)