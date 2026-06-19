import torch
y = torch.tensor([1, 4, 9, 16])
x = torch.tensor([0, 1, 2, 3])
result = torch.cumulative_trapezoid(y=y, x=x)
print(result)