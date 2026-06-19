import torch
from torch.nn.utils.prune import random_unstructured
model = torch.nn.Linear(10, 5)
params_to_prune = ((model, 'weight'),)