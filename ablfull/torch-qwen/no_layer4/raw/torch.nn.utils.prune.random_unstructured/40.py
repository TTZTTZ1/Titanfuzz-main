import torch
from torch.nn import Linear

module = Linear(10, 5)
name = 'weight'
amount = 0.5

torch.nn.utils.prune.random_unstructured(module, name, amount)