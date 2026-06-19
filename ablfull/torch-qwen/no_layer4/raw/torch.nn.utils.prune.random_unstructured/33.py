import torch
from torch.nn.utils import prune

# Create a simple model
model = torch.nn.Linear(5, 3)

# Prepare input parameters
name = 'weight'
amount = 0.5

# Call the API
prune.random_unstructured(model, name, amount)