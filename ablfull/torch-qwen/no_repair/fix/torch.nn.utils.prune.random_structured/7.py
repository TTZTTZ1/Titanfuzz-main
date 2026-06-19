
import torch
from torch.nn.utils.prune import random_structured
model = torch.nn.Linear(4, 2)
name = 'weight'
amount = 0.5
dim = 0
random_structured(model, name, amount, dim)
