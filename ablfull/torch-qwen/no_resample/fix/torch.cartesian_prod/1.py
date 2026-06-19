import torch
a = torch.tensor([1, 2])
b = torch.tensor([3, 4])
result = torch.cartesian_prod(a, b)
print(result)