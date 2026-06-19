import torch
from torch.nn.utils import prune
model = torch.nn.Linear(10, 5)
name = 'weight'
amount = 0.5
dim = 1
prune.random_structured(model, name, amount=amount, dim=dim)