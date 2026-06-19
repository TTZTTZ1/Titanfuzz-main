import torch

x = torch.tensor(1.0)
result = torch.special.i1e(x)
print(result)