import torch
from torch.nn.utils import prune

# Create a simple model for demonstration
model = torch.nn.Linear(5, 3)

# Prepare valid input data
name = 'weight'
amount = 0.5
dim = 0

# Call the API
prune.random_structured(model, name, amount=amount, dim=dim)