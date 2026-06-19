
import torch
y = torch.tensor([1, 4, 9], dtype=torch.float)
dx = 1.0
dim = 0
result = torch.cumulative_trapezoid(y=y, dx=dx, dim=dim)
print(result)
