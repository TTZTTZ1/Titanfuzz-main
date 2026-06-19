import torch
from torch.nn import Linear
from torch.nn.utils import prune

# Prepare input data
module = Linear(10, 5)
name = 'weight'
amount = 0.5
dim = 0

# Call the API
pruned_module = prune.random_structured(module, name, amount, dim=dim)