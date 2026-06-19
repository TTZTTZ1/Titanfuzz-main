import torch
from torch.nn.utils import prune

# Prepare valid input data
module = torch.nn.Linear(10, 5)
name = 'weight'
amount = 0.2
dim = 1

# Call the API
prune.random_structured(module, name, amount=amount, dim=dim)