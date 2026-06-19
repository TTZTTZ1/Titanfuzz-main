
import torch
p = 0.7
result = torch.tensor([1.0, 0.0]).bernoulli_(p)
print(result)
