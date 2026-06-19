import torch
p = 0.7
result = torch.tensor([0.1, 0.9]).bernoulli_(p)
print(result)