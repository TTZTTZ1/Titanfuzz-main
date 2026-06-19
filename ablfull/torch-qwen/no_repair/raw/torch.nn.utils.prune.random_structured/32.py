import torch
from torch.nn.modules.module import Module

# Task 2: Generate input data
module = Module()  # Replace with your actual module
name = 'weight'
amount = 0.5
dim = 0

# Task 3: Call the API
torch.nn.utils.prune.random_structured(module, name, amount, dim)