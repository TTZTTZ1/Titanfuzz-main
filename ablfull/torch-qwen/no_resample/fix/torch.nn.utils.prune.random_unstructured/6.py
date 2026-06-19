import torch
from torch.nn.utils import prune
model = torch.nn.Linear(5, 2)
name = 'weight'
amount = 0.5
prune.random_unstructured(model, name, amount)