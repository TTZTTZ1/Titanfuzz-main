
import torch
y = torch.tensor([[1, 2], [3, 4]])
dx = 0.5
result = torch.cumulative_trapezoid(y, dx=dx)
print(result)
