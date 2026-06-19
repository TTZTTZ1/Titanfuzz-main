import torch
from torch.nn.utils import prune
module = torch.nn.Linear(10, 5)
params_to_prune = (module, 'weight')
prune.random_unstructured(*params_to_prune, amount=0.1)