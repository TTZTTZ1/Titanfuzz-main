import torch
x = torch.tensor([0, 1, 2, 3])
y = torch.tensor([4, 5, 6, 7])
result = torch.cumulative_trapezoid(y, x)
print(result)