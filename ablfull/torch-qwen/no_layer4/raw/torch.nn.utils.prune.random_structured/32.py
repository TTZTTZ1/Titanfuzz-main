import torch
from torch.nn.utils import prune

# Create a simple model for pruning
model = torch.nn.Linear(5, 2)
name = 'weight'
amount = 0.5
dim = 0

prune.random_structured(model, name, amount=amount, dim=dim)