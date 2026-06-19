import torch
from torch.nn.utils import prune

# Create a simple model
model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)

# Prepare input parameters
name = '0.0'
amount = 0.5
dim = 0

# Call the API
prune.random_structured(model, name, amount, dim)