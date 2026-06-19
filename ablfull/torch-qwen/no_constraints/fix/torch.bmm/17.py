import torch
a = torch.randn(10, 5, 3)
b = torch.randn(10, 3, 4)
result = torch.bmm(a, b)