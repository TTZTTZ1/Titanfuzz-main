import torch
from torch.nn.utils.prune import random_unstructured
model = torch.nn.Linear(5, 3)
params_to_prune = ((model, 'weight'),)
pruning_magnitude = 0.5