import torch
from torch.nn.utils import prune
module = torch.nn.Linear(10, 5)
name = 'weight'
amount = 0.5
pruned_module = prune.random_unstructured(module, name, amount=amount)