import torch
import torch.nn as nn

# Create a simple model for pruning
model = nn.Sequential(
    nn.Linear(10, 20),
    nn.ReLU(),
    nn.Linear(20, 5)
)

# Prepare input parameters
module = model[0]  # Selecting the first layer for pruning
name = 'weight'
amount = 0.5  # Valid float between 0.0 and 1.0

# Call the API
pruned_module = nn.utils.prune.random_unstructured(module, name=name, amount=amount)