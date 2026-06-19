
import torch
from torch.nn.utils import prune
model = torch.nn.Linear(10, 5)
module = model
name = 'weight'
amount = 0.5
prune.random_unstructured(module, name, amount)
