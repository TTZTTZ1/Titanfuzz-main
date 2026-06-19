import torch
from torch.nn.utils import prune

# Prepare valid input data
module = torch.nn.Linear(10, 5)
params_to_prune = ('weight',)
amount = 0.2

# Call the API
prune.random_structured(module, params_to_prune, amount=amount)