
import torch
y = torch.tensor([1.0, 2.5, 4.0, 6.5])
x = torch.tensor([0.0, 1.0, 2.0, 3.0])
result = torch.cumulative_trapezoid(y=y, x=x)
print(result)
