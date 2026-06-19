import torch

x = torch.tensor([0., 1., 2., 3., 4.], dtype=torch.float64)
y = torch.tensor([0., 1., 4., 9., 16.], dtype=torch.float64)

result = torch.cumulative_trapezoid(y=y, x=x, dx=None)