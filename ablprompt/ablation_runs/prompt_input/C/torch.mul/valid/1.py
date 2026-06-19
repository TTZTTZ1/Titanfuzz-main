import torch

a = torch.randn(3, 3)
b = torch.randn(3, 3)
result = torch.mul(a, b)
print(result)