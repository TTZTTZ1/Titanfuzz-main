import torch
p = 0.7
result = torch.tensor([0.1, 0.4, 0.6]).bernoulli_(p)
print(result)