import torch

a = torch.tensor([1, 2])
b = torch.tensor([3.0, 4.0])
result = torch.cartesian_prod(a, b)
print(result)