import torch

# Create two tensors
a = torch.randn(3, 4, dtype=torch.float32)
b = torch.randn(4, dtype=torch.float32)

# Perform element-wise multiplication
result = torch.mul(a, b)

print(result)