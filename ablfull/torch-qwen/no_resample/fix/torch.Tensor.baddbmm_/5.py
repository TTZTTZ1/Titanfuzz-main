import torch
a = torch.randn(3, 4, 5)
b = torch.randn(3, 5, 6)
c = torch.randn(3, 4, 6)
result = c.baddbmm_(a, b, beta=1, alpha=1)