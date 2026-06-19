import torch
from torch.nn.utils import prune

# Create a simple model
model = torch.nn.Linear(5, 1)

# Prepare valid input data
module = model
name = 'weight'
amount = 0.5

# Call the API
prune.random_unstructured(module, name, amount)