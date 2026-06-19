import torch
a = torch.randn(10, 3, 5)
b = torch.randn(10, 5, 4)
result = torch.bmm(a, b)