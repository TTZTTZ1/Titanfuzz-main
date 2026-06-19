import torch

a = torch.arange(16).reshape(4, 4)
result = torch.split(a, [3, 1], dim=1)
print(result)