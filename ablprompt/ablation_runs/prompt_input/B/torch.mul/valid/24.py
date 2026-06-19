import torch

a = torch.randn(3, 4, 5)
b = torch.randn(4, 5)
c = torch.randn(3, 4, 5)

result = torch.mul(torch.mul(a, b), c)
print(result)