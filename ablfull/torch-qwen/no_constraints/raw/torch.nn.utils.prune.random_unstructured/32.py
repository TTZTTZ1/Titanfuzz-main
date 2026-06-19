import torch
from torch.nn.utils import prune

# Prepare valid input data
module = torch.nn.Linear(in_features=5, out_features=3)
params_to_prune = (module, 'weight')
pruning_method = prune.RandomUnstructured
amount = 0.2

# Call the API
prune.random_unstructured(params_to_prune[0], name=params_to_prune[1], amount=amount, pruning_method=pruning_method)