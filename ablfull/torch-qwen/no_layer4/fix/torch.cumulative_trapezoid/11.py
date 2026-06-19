import torch
y = torch.tensor([1, 4, 5, 8])
dx = 0.5
dim = 0
result = torch.cumulative_trapezoid(y, dx=dx, dim=dim)
print(result)