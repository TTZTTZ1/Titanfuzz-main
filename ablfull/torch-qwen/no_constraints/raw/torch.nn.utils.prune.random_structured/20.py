import torch
from torch.nn.utils import prune

# Task 2: Generate input data
module = torch.nn.Linear(5, 3)
params_to_prune = ('weight',)
pruning_magnitude = 0.2

# Task 3: Call the API
prune.random_structured(module, params_to_prune, pruning_magnitude=pruning_magnitude)