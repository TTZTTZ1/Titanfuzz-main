import torch
from torch.nn.utils.prune import random_unstructured
module = torch.nn.Linear(5, 2)
name = 'weight'
amount = 0.5
random_unstructured(module, name, amount=amount)