import torch
from torch.nn.utils import prune

# Create a sample module
model = torch.nn.Linear(10, 5)

# Prepare valid input data
module = model
name = 'weight'
amount = 0.2
dim = 1

# Call the target API
prune.random_structured(module, name, amount=amount, dim=dim)