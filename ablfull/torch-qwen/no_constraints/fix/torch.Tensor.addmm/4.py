import torch
a = torch.randn(3, 4)
b = torch.randn(3, 2)
c = torch.randn(2, 4)
result = a.addmm(b, c)