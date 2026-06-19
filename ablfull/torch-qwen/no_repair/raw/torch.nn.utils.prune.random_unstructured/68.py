import torch
from torch.nn.utils import prune

# Task 2: Generate input data
module = torch.nn.Linear(10, 5)
name = 'weight'
amount = 0.5

# Task 3: Call the API
prune.random_unstructured(module, name, amount)