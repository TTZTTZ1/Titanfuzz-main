import torch
a = torch.randn(2, 1, 3)
b = torch.randn(2, 3, 4)
result = torch.bmm(a, b)