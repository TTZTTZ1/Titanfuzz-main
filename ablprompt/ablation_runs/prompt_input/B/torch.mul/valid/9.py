import torch

a = torch.randn(3, 4)
b = torch.randn(4)
c = torch.randn(3, 4)

result = torch.mul(torch.mul(a, b), c)
print(result)