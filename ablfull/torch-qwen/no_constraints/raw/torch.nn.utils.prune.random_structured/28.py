import torch
import torch.nn as nn

# Define a simple model
model = nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    nn.Linear(5, 2)
)

# Prepare input data
input_data = torch.randn(1, 10)

# Apply random structured pruning to the first linear layer
prune.random_structured(model[0], name='weight', amount=0.2)