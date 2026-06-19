import torch
x = torch.tensor([1.5, (- 2.3), 0.7])
result = torch.special.round(x)
print(result)