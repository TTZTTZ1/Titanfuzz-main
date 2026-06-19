import torch
from torch.nn import Linear

module = Linear(in_features=10, out_features=5)
name = 'weight'
amount = 0.5
dim = 1

pruned_module = torch.nn.utils.prune.random_structured(module, name, amount, dim)