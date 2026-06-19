import torch
import torch.nn as nn

# Task 2: Generate input data
model = nn.Linear(10, 5)
name = 'weight'
amount = 0.5

# Task 3: Call the API
torch.nn.utils.prune.random_unstructured(model, name, amount)