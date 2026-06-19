import torch
import torch.nn as nn

# Create a simple model for pruning
model = nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    nn.Linear(5, 2)
)

# Prepare valid input data
name = 'linear_0'
amount = 0.3

# Call the API
pruned_model = nn.utils.prune.random_unstructured(model, name=name, amount=amount)