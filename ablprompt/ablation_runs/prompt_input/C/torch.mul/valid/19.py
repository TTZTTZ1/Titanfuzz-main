import torch

a = torch.randn(3, 4, dtype=torch.float32)
b = torch.randn(4, dtype=torch.float32)
result = torch.mul(a, b)
print(result)