import torch
from torch.nn.utils.prune import random_structured

# Prepare valid input data
model = torch.nn.Linear(10, 5)
name = 'weight'
amount = 0.2

# Call the API
random_structured(model, name, amount=amount)