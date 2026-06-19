import torch
import torch.nn as nn
from torch.nn.utils import prune
module = nn.Linear(10, 5)
name = 'weight'
amount = 0.5
prune.random_unstructured(module, name, amount)