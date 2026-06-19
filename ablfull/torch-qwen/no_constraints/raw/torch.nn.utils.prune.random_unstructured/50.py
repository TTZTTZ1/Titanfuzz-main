import torch
from torch.nn.utils import prune

# Task 2: Generate input data
module = torch.nn.Linear(in_features=10, out_features=5)
pruning_magnitude = 0.5

# Task 3: Call the API
pruned_module = prune.random_unstructured(module, name='weight', amount=pruning_magnitude)