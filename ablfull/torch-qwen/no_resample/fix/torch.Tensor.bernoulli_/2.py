import torch
p = 0.7
result = torch.tensor([0.5, 0.8]).bernoulli_(p)
print(result)