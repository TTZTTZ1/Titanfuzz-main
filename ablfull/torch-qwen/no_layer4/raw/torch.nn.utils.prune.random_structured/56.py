import torch
from torch.nn.utils import prune

# Create a simple model for pruning
model = torch.nn.Sequential(
    torch.nn.Linear(5, 3),
    torch.nn.ReLU(),
    torch.nn.Linear(3, 1)
)

# Prepare input data
name = '0'
amount = 0.5
dim = 0

# Call the API
prune.random_structured(model, name, amount, dim=dim)