import torch
p = torch.tensor([0.5])
result = torch.tensor([0.0]).bernoulli_(p)
print(result)