import torch
from torch.nn.utils import prune

# Create a simple model
model = torch.nn.Linear(10, 5)

# Prepare valid input data
name = 'weight'
amount = 0.5
dim = 1

# Call the API
prune.random_structured(model, name, amount=amount, dim=dim)