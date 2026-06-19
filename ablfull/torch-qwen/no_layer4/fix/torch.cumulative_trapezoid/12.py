import torch
y = torch.tensor([1, 4, 5, 8], dtype=torch.float)
dx = 0.5
dim = (- 1)
result = torch.cumulative_trapezoid(y=y, dx=dx, dim=dim)
print(result)