import torch
from torch.nn.utils import prune

# Task 2: Generate input data
model = torch.nn.Linear(10, 5)
params_to_prune = (model.weight,)
pruning_magnitude = 0.5

# Task 3: Call the API
prune.random_structured(params_to_prune, name='weight', amount=pruning_magnitude)