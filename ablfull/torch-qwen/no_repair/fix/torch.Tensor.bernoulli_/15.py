
import torch
p = torch.tensor(0.7)
result = torch.rand_like(p)
result.bernoulli_(p)
