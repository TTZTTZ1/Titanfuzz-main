import torch
a = torch.randn(2, 3, 5)
b = torch.randn(2, 5, 4)
result = torch.bmm(a, b)