
import torch
a = torch.randn(3, 4)
b = torch.randn(4, 5)
result = torch.Tensor.mm(a, b)
