import torch
x = torch.tensor([0.5], dtype=torch.float32)
result = torch.special.i1e(x)
print(result)