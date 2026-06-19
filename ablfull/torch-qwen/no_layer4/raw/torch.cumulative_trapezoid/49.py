import torch

y = torch.tensor([1, 2, 4, 7, 11])
x = torch.tensor([0, 1, 2, 3, 4], dtype=torch.float)
dx = 1.0
dim = -1

result = torch.cumulative_trapezoid(y, x, dx, dim)
print(result)