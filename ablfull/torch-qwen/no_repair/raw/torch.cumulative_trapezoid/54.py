import torch

y = torch.tensor([[1, 2, 4], [5, 6, 8]], dtype=torch.float)
x = None
dx = 1.0
dim = 1

result = torch.cumulative_trapezoid(y, x=x, dx=dx, dim=dim)
print(result)