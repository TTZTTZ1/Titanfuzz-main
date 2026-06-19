import torch
y = torch.tensor([1, 2, 4, 7], dtype=torch.float)
x = torch.tensor([0, 1, 2, 3], dtype=torch.float)
dim = 0
result = torch.cumulative_trapezoid(y, x=x, dim=dim)
print(result)