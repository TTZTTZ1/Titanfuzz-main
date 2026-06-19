import torch
from torch.nn.utils.prune import random_structured

# Create a simple linear model as the module
model = torch.nn.Linear(4, 2)

# Prepare valid input data
name = 'weight'
amount = 0.5
dim = 0

# Call the API
random_structured(model, name, amount, dim)