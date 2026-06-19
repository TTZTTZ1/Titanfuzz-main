import torch
from torch.nn.utils import prune

# Prepare input data
module = torch.nn.Linear(5, 1)
name = 'weight'
amount = 0.5

# Call the API
prune.random_unstructured(module, name, amount)