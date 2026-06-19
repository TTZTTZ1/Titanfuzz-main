import torch
import torch.nn as nn

# Task 2: Generate input data
module = nn.Linear(5, 3)
name = 'weight'
amount = 0.5

# Task 3: Call the API
torch.nn.utils.prune.random_unstructured(module, name, amount)