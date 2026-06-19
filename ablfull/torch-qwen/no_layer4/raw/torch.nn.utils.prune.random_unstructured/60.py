import torch
from torch.nn import Linear

# Task 2: Generate input data
module = Linear(in_features=10, out_features=5)
name = 'weight'
amount = 0.5

# Task 3: Call the API
torch.nn.utils.prune.random_unstructured(module, name, amount)