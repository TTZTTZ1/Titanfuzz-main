import torch
from torch.nn.utils import prune

# Create a sample module
module = torch.nn.Linear(10, 5)

# Prepare valid input data
name = 'weight'
amount = 0.5

# Call the API
prune.random_unstructured(module, name, amount)