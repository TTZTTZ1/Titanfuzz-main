import torch

y = torch.tensor([1.0, 2.0, 4.0, 7.0])
dx = 1.0
dim = -1

result = torch.cumulative_trapezoid(y, dx=dx, dim=dim)