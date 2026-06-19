
import torch
x = torch.randn(2, 3, 4)
dims = (1, 0, 2)
result = x.permute(dims)
