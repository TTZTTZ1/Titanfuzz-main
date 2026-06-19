import torch
from torch.nn.utils import prune
model = torch.nn.Linear(10, 5)
params_to_prune = (model, 'weight')
prune.random_unstructured(*params_to_prune, amount=0.3)