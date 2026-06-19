import torch
import torch.nn as nn

# Create a simple model
model = nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    nn.Linear(5, 2)
)

# Prepare input parameters
name = '0'  # Assuming we want to prune the first layer
amount = 0.5  # Pruning half of the connections
dim = 1  # Pruning along the second dimension (input size)

# Call the API
torch.nn.utils.prune.random_structured(model[0], name, amount=amount, dim=dim)