import torch
a = torch.tensor([1, 2], dtype=torch.float)
b = torch.tensor([3, 4], dtype=torch.float)
result = torch.cartesian_prod(a, b)
print(result)