import torch
import torch.nn as nn

# Define a simple model to prune
model = nn.Sequential(
    nn.Linear(5, 3),
    nn.ReLU(),
    nn.Linear(3, 1)
)

# Prepare valid input data
amount = 0.5

# Call the API
pruned_model = nn.utils.prune.random_unstructured(model, name='0', amount=amount)