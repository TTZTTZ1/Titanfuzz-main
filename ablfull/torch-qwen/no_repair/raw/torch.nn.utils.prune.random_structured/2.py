import torch
from torch.nn.utils import prune

# Prepare input data
module = torch.nn.Linear(10, 5)
name = 'weight'
amount = 0.5
dim = 0

# Call the API
prune.random_structured(module, name, amount, dim)