import torch
from torch.nn.utils.prune import random_structured
module = torch.nn.Linear(5, 3)
amount = 0.3
name = 'weight'
pruning_method = random_structured