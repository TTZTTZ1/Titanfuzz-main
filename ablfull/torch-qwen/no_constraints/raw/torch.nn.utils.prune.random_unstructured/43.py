import torch
from torch.nn.utils import prune

# Generate input data
module = torch.nn.Linear(10, 5)
pruning_amount = 0.3

# Call the API
pruned_module = prune.random_unstructured(module, name='weight', amount=pruning_amount)