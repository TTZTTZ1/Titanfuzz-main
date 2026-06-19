import torch
from torch.nn.utils import prune

# Create a simple model to apply pruning on
model = torch.nn.Sequential(torch.nn.Linear(10, 5), torch.nn.ReLU(), torch.nn.Linear(5, 2))

# Prepare input parameters
module = model[0]  # Choosing the first layer for pruning
name = 'weight'  # Weights of the chosen layer
amount = 0.5  # Pruning ratio

# Call the API
prune.random_unstructured(module, name, amount)