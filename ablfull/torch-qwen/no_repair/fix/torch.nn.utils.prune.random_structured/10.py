
import torch
from torch.nn.utils import prune
module = torch.nn.Linear(5, 3)
name = 'weight'
amount = 0.5
dim = 0
prune.random_structured(module, name, amount, dim)
