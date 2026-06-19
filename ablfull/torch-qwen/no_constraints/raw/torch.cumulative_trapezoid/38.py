import torch

y = torch.tensor([0., 1., 4., 9.], dtype=torch.float64)
x = torch.tensor([0., 1., 2., 3.], dtype=torch.float64)

result = torch.cumulative_trapezoid(y, x, initial=0.)