import torch
p = 0.75
result = torch.tensor([0, 1]).bernoulli_(p)
print(result)