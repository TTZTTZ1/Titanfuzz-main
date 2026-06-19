import torch
from torch.nn.utils import prune

# Prepare valid input data
module = torch.nn.Linear(10, 5)
params_to_prune = ('weight', 'bias')
pruning_method = prune.RandomUnstructured

# Call the API
pruned_module = prune.random_unstructured(module, name='weight', amount=0.2)