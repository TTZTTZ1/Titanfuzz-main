import torch
from torch.nn.utils import prune

# Create a simple model for demonstration
model = torch.nn.Sequential(
    torch.nn.Linear(4, 8),
    torch.nn.ReLU(),
    torch.nn.Linear(8, 2)
)

# Prepare valid input data
name = '0.weight'
amount = 0.5

# Call the API
prune.random_unstructured(model[0], name=name, amount=amount)