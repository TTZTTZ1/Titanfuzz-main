import torch
y = torch.tensor([1.0, 2.0, 4.0, 7.0], dtype=torch.float)
dx = 0.5
dim = 0
result = torch.cumulative_trapezoid(y, dx=dx, dim=dim)
print(result)