import torch
from torch.nn.utils import prune

# Task 2: Generate input data
module = torch.nn.Linear(10, 5)
params_to_prune = ('weight',)
amount = {name: 0.2 for name, _ in params_to_prune}

# Task 3: Call the API
pruned_module = prune.random_structured(module, params_to_prune[0], amount=params_to_prune[1])