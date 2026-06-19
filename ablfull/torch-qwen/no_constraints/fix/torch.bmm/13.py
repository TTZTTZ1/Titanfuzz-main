import torch
x = torch.randn(2, 3, 4)
y = torch.randn(2, 4, 5)
result = torch.bmm(x, y)