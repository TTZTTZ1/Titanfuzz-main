import torch
from torch.nn.utils import prune

# Create a simple model
model = torch.nn.Sequential(
    torch.nn.Linear(10, 20),
    torch.nn.ReLU(),
    torch.nn.Linear(20, 2)
)

# Define input parameters
name = '0.0'
amount = 0.5
dim = 0

# Apply pruning
prune.random_structured(model[0], name, amount=amount, dim=dim)