import torch
from torch.nn.utils import prune

# Prepare valid input data
model = torch.nn.Linear(10, 5)
params_to_prune = (model.weight,)
pruning_method = prune.L1Unstructured
amount = 0.3

# Call the API
prune.random_structured(params_to_prune, pruning_method, amount=amount)