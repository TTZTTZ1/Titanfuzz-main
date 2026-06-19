import torch
from torch.nn.utils import prune
model = torch.nn.Linear(5, 1)
module = model
name = 'weight'
amount = 0.5
prune.random_unstructured(module, name, amount)