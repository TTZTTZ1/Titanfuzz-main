import torch

x = torch.tensor([1.0, 2.0, 4.0, 7.0], dtype=torch.float64)
y = torch.tensor([10.0, 15.0, 20.0, 25.0], dtype=torch.float64)
result = torch.cumulative_trapezoid(y, x, initial=0.0)