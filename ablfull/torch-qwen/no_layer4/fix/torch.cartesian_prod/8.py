import torch
x = torch.tensor([1, 2])
y = torch.tensor([3, 4])
result = torch.cartesian_prod(x, y)
print(result)