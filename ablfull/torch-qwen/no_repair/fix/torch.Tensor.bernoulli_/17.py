
import torch
p = torch.tensor(0.7)
result = torch.empty((3, 3)).bernoulli_(p)
