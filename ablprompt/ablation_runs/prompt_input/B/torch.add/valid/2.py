import torch

a = torch.randn(3, 4)
b = torch.randn(4)
c = torch.add(a, b, alpha=0.5)
print(c)