import torch
import torch.nn as nn

# Create a sample module
module = nn.Linear(10, 5)

# Prepare valid input data
name = 'weight'
amount = 0.3
dim = 1

# Call the API
pruned_module = nn.utils.prune.random_structured(module, name, amount, dim)