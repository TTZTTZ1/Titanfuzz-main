import torch
x = torch.tensor([0.0, 1.0, 2.0, 3.0], dtype=torch.float32)
y = torch.tensor([0.0, 4.0, 9.0, 16.0], dtype=torch.float32)
result = torch.cumulative_trapezoid(y, x)
print(result)