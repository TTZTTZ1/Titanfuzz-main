import torch
from torch.nn.utils import prune

# Prepare valid input data
module = torch.nn.Linear(in_features=5, out_features=2)
name = 'weight'

# Call the API
pruned_module = prune.random_unstructured(module, name=name, amount=0.1)