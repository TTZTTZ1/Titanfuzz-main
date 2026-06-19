import torch
from torch.nn.utils import prune

# Create a simple model
model = torch.nn.Linear(5, 2)

# Prepare input data
name = 'weight'
amount = 0.5
dim = 0

# Call the API
prune.random_structured(model, name, amount, dim)