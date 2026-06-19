import torch
a = torch.randn(5, 4)
b = torch.randn(4, 3)
result = torch.Tensor.mm(a, b)