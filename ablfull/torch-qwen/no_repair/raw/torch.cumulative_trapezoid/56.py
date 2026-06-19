import torch

y = torch.tensor([1.0, 2.0, 4.0, 8.0], dtype=torch.float)
dx = 2.0
dim = -1

result = torch.cumulative_trapezoid(y, dx=dx, dim=dim)
print(result)