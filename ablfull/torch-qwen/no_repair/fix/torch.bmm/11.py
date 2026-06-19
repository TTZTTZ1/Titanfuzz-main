
import torch
a = torch.randn(5, 3, 4)
b = torch.randn(5, 4, 6)
result = torch.bmm(a, b)
