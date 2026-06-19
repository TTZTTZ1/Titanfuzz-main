import torch
from torch.nn import Linear

# Create a sample model
model = Linear(10, 5)

# Prepare input data for the function
module = model
name = 'weight'
amount = 0.5
dim = 0

# Call the API
torch.nn.utils.prune.random_structured(module, name, amount, dim)