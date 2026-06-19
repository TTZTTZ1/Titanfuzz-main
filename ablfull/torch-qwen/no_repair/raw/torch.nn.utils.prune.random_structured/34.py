import torch
from torch.nn.utils import prune

# Task 2: Generate input data
module = torch.nn.Linear(in_features=5, out_features=3)
name = 'weight'
amount = 0.5
dim = 0

# Task 3: Call the API
prune.random_structured(module, name, amount, dim)