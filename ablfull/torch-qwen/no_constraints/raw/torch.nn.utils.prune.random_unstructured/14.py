import torch
from torch.nn.utils import prune

# Define a simple model
model = torch.nn.Linear(10, 2)

# Prepare input data
weight = model.weight.data.clone()

# Call the API
pruned_weight = prune.random_unstructured(weight, name='weight', amount=0.5)