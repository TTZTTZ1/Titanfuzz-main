import torch
from torch.nn.utils import prune

# Create a sample module
module = torch.nn.Linear(10, 5)

# Prepare input data
name = 'weight'
amount = 0.5
dim = 0

# Call the API
pruned_module = prune.random_structured(module, name, amount, dim)