import torch
from torch.nn.utils import prune

module = torch.nn.Linear(10, 5)
name = 'weight'
amount = 0.5

prune.random_unstructured(module, name, amount)