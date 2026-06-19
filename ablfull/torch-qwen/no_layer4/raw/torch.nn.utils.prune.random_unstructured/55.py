import torch
from torch.nn.utils.prune import random_unstructured

# Create a simple example module
module = torch.nn.Linear(5, 2)

# Prepare input data
name = 'weight'
amount = 0.5

# Call the API
random_unstructured(module, name, amount)