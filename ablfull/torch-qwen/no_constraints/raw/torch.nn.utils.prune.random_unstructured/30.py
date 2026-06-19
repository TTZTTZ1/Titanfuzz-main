import torch
from torch.nn.utils import prune

# Define a simple model
model = torch.nn.Linear(5, 2)

# Prepare input data
input_data = torch.randn(10, 5)

# Apply random unstructured pruning to the model's weight
prune.random_unstructured(model.weight, name='weight', amount=0.3)