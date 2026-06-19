import torch
from torch.nn.utils import prune

# Create a simple model
model = torch.nn.Linear(10, 5)

# Prepare input data
name = 'weight'
amount = 0.5

# Call the API
prune.random_unstructured(model, name, amount)