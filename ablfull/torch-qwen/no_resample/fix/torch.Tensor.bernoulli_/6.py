import torch
p = 0.7
result = torch.tensor([0.3, 0.8, 0.4]).bernoulli_(p)
print(result)