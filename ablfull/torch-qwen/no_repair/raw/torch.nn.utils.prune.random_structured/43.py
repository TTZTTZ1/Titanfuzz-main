import torch
from torch.nn import Linear

module = Linear(in_features=5, out_features=2)
name = 'weight'
amount = 0.5
dim = 0

torch.nn.utils.prune.random_structured(module, name, amount, dim)