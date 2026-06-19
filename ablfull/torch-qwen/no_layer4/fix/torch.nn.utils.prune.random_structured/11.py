import torch
from torch.nn import Linear
from torch.nn.utils import prune
module = Linear(10, 5)
name = 'weight'
amount = 0.5
dim = 0
pruned_module = prune.random_structured(module, name, amount, dim=dim)