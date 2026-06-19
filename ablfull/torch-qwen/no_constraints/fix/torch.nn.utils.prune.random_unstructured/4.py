import torch
from torch.nn.utils.prune import random_unstructured
module = torch.nn.Linear(in_features=10, out_features=5)
params_to_prune = (module, 'weight')