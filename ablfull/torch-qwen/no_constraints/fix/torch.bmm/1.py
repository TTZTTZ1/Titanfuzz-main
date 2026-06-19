import torch
a = torch.randn(10, 3, 4)
b = torch.randn(10, 4, 5)
result = torch.bmm(a, b)