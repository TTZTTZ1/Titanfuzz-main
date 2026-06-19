import torch
from torch.nn import Linear

# Create a sample model
model = Linear(10, 5)

# Prepare valid input data
module = model
name = 'weight'
amount = 0.5

# Call the API
pruned_module = torch.nn.utils.prune.random_unstructured(module, name, amount)