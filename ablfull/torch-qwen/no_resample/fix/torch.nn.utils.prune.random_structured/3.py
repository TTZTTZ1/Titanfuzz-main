import torch
import torch.nn as nn
from torch.nn.utils import prune
model = nn.Linear(10, 5)
name = 'weight'
amount = 0.5
dim = 0
pruned_model = prune.random_structured(model, name, amount, dim)