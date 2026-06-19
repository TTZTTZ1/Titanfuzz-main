import torch
import torch.nn as nn

# Task 2: Generate input data
model = nn.Linear(5, 3)
params_to_prune = (model.weight,)
pruning_magnitude = 0.2

# Task 3: Call the API
torch.nn.utils.prune.random_unstructured(params_to_prune, name='weight', amount=pruning_magnitude)