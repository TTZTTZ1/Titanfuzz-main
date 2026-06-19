import torch
y = torch.tensor([1.0, 2.0, 4.0])
x = torch.tensor([1.0, 2.0, 3.0])
result = torch.cumulative_trapezoid(y, x)