import torch
p = 0.75
result = torch.tensor([0.1, 0.4, 0.8]).bernoulli_(p)
print(result)