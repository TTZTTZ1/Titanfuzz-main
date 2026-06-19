import torch
p = 0.7
generator = None
result = torch.tensor([0.5, 0.8]).bernoulli_(p, generator=generator)
print(result)