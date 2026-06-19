import torch
from torch.nn.utils import prune

# Create a simple model for demonstration
model = torch.nn.Linear(10, 5)

# Prepare valid input data
module = model
name = 'weight'
amount = 0.5

# Call the API
pruned_module = prune.random_unstructured(module, name, amount)