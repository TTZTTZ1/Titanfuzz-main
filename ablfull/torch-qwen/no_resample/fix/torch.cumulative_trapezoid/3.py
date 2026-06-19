import torch
y = torch.tensor([1, 2, 4, 7], dtype=torch.float)
dx = 1.0
dim = (- 1)
result = torch.cumulative_trapezoid(y, dx=dx, dim=dim)
print(result)