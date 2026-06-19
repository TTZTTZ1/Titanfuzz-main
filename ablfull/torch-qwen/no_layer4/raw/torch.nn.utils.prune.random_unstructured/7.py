import torch
from torch.nn.utils import prune

# Create a simple model
model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)

# Prepare input data
name = 'linear'
amount = 0.5

# Call the API
prune.random_unstructured(model[name], name='weight', amount=amount)