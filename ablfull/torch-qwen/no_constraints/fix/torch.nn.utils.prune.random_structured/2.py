import torch
from torch.nn.utils.prune import random_structured
model = torch.nn.Linear(10, 5)
name = 'weight'
amount = 0.2