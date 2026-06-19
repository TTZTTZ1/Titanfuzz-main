import torch

y = torch.tensor([1, 4, 9, 16], dtype=torch.float)
dx = 0.5
dim = 0

result = torch.cumulative_trapezoid(y, dx=dx, dim=dim)