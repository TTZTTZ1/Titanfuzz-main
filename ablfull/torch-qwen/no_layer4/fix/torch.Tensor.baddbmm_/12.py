import torch
a = torch.randn(4, 5, 6)
b = torch.randn(4, 6, 7)
c = torch.randn(4, 5, 7)
result = c.baddbmm_(a, b, beta=2, alpha=3)