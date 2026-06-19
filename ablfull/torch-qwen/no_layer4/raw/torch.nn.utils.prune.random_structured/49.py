import torch
import torch.nn as nn
from torch.nn.utils import prune

# Define a simple model
model = nn.Sequential(nn.Linear(10, 5), nn.ReLU(), nn.Linear(5, 2))

# Prepare input data
name = 'linear'  # Assuming we want to prune the first linear layer named 'linear'
amount = 0.3  # Pruning 30% of the weights
dim = 0  # Pruning along the first dimension

# Call the API
prune.random_structured(model, name, amount, dim)