import torch
from torch.nn.utils import prune

# Create a simple model
model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)

# Define parameters for the pruning function
name = '0'
amount = 0.5

# Apply random unstructured pruning
prune.random_unstructured(model[0], name=name, amount=amount)