import torch
from torch.nn.utils.prune import random_unstructured
module = torch.nn.Linear(5, 3)
name = 'weight'
amount = 0.5
random_unstructured(module, name, amount=amount)