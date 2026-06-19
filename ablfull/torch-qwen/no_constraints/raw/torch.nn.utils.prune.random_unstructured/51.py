import torch
from torch.nn.utils.prune import random_unstructured

# Task 2: Generate input data
model = torch.nn.Linear(5, 3)
params_to_prune = ((model, 'weight'),)
pruning_magnitude = 0.5

# Task 3: Call the API
random_unstructured(params_to_prune, name='weight', amount=pruning_magnitude)