import torch
y = torch.tensor([0.0, 1.0, 4.0, 9.0])
x = torch.tensor([0.0, 1.0, 2.0, 3.0])
result = torch.cumulative_trapezoid(y, x)