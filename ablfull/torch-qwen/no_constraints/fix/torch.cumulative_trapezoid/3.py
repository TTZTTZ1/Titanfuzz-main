import torch
x = torch.tensor([0.0, 1.0, 2.0, 3.0], dtype=torch.float64)
y = torch.tensor([0.0, 1.0, 4.0, 9.0], dtype=torch.float64)
result = torch.cumulative_trapezoid(y, x, axis=(- 1))
print(result)