import torch
y = torch.tensor([1, 2, 4, 7])
dx = 0.5
dim = 0
result = torch.cumulative_trapezoid(y=y, dx=dx, dim=dim)
print(result)