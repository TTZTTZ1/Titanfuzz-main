import torch
import torch.nn as nn

# Create a simple model
model = nn.Linear(10, 5)

# Prepare valid input data
name = 'weight'
amount = 0.5
dim = 0

# Call the API
torch.nn.utils.prune.random_structured(model, name, amount, dim)