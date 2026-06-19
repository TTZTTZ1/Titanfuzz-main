
import torch
from torch.nn.utils import prune
model = torch.nn.Linear(5, 3)
name = 'weight'
amount = 0.5
dim = 0
prune.random_structured(model, name, amount=amount, dim=dim)
