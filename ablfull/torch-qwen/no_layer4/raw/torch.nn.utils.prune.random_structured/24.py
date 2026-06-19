import torch
import torch.nn as nn

# Create a simple model
model = nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    nn.Linear(5, 2)
)

# Prepare input data
name = 'linear'
amount = 0.5
dim = 0

# Call the API
pruned_model = torch.nn.utils.prune.random_structured(model, name, amount, dim)