
import torch
a = torch.randn(5, 3, 4)
b = torch.randn(5, 4, 6)
c = torch.bmm(a, b)
