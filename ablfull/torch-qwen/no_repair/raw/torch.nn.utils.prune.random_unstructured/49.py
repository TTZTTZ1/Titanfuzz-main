import torch
from torch.nn.utils import prune

# Create a simple model
model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)

# Prepare input parameters
name = 'linear'
amount = 0.5

# Call the API
pruned_model = prune.random_unstructured(model, name=name, amount=amount)