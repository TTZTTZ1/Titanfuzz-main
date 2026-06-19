import torch
import torch.nn as nn

# Create a simple model for demonstration
model = nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    nn.Linear(5, 1)
)

# Prepare input data
name = 'linear'
amount = 0.2
dim = 0

# Call the API
torch.nn.utils.prune.random_structured(model, name, amount, dim=dim)