import torch
import torch.nn as nn

module = nn.Linear(10, 5)
name = 'weight'
amount = 0.3
dim = 1

nn.utils.prune.random_structured(module, name, amount=amount, dim=dim)