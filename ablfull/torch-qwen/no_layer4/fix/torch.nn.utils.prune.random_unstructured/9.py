import torch
from torch.nn.utils import prune
model = torch.nn.Sequential(torch.nn.Linear(10, 5), torch.nn.ReLU(), torch.nn.Linear(5, 2))
module = model[0]
name = 'weight'
amount = 0.5
prune.random_unstructured(module, name, amount)