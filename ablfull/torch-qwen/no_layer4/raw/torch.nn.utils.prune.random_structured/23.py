import torch
import torch.nn as nn
from torch.nn.utils import prune

# Create a simple model
model = nn.Linear(10, 5)

# Prepare input data
name = 'weight'
amount = 0.5
dim = 0

# Call the API
prune.random_structured(model, name, amount, dim)