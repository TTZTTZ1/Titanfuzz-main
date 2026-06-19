import torch

x = torch.tensor([0., 1., 2., 3.], dtype=torch.float32)
y = torch.tensor([0., 2., 4., 6.], dtype=torch.float32)
result = torch.cumulative_trapezoid(y, x, dx=1.0, axis=-1, initial=None)