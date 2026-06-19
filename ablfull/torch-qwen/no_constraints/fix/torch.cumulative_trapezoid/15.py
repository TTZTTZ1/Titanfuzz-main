import torch
x = torch.tensor([0, 1, 2], dtype=torch.float32)
y = torch.tensor([1, 4, 9], dtype=torch.float32)
result = torch.cumulative_trapezoid(y, x)