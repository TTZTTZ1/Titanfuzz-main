import torch
from torch.nn.utils.prune import random_unstructured

# Task 2: Generate input data
module = torch.nn.Linear(5, 3)
name = 'weight'
amount = 0.5

# Task 3: Call the API
random_unstructured(module, name, amount=amount)