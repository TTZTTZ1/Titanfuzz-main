import torch
from torch.nn.utils import prune

# Create a sample model
model = torch.nn.Linear(10, 5)

# Prepare input data
module = model
name = 'weight'
amount = 0.5

# Call the API
prune.random_unstructured(module, name, amount)