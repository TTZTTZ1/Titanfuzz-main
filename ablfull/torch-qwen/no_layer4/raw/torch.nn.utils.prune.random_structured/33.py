import torch
import torch.nn as nn

# Prepare valid input data
module = nn.Linear(10, 5)
name = 'weight'
amount = 0.5
dim = 0

# Call the API
torch.nn.utils.prune.random_structured(module, name, amount, dim=dim)