
import torch
t = torch.randn(3, 4, 5)
a = torch.randn(3, 4, 6)
b = torch.randn(3, 6, 5)
result = t.baddbmm_(a, b, beta=1, alpha=1)
