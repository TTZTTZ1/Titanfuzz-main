import torch
from torch.nn.utils.prune import random_structured

# Prepare input data
module = torch.nn.Linear(5, 3)
amount = 0.3
name = 'weight'
pruning_method = random_structured

# Call the API
random_structured(module, name, amount, pruning_method=pruning_method)