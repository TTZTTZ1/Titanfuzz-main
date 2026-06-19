import torch
from torch.nn import Linear

# Create a sample model
model = Linear(in_features=10, out_features=5)

# Prepare valid input data
name = 'weight'
amount = 0.5

# Call the API
pruned_model = torch.nn.utils.prune.random_unstructured(model, name=name, amount=amount)