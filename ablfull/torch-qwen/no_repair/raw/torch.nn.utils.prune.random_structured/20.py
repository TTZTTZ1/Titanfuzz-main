import torch
from torch.nn.utils import prune

# Create a simple model for demonstration
model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)

# Prepare valid input data
name = 'linear_0.weight'
amount = 0.3
dim = 0

# Call the API
prune.random_structured(model, name, amount, dim)