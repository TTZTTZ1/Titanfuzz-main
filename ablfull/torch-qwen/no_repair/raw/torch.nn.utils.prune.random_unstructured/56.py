import torch
from torch.nn.utils import prune

# Prepare valid input data
module = torch.nn.Linear(10, 5)
name = 'weight'
amount = 0.5

# Call the API
prune.random_unstructured(module, name, amount)