import torch
from torch.nn.utils import prune

# Task 2: Generate input data
model = torch.nn.Linear(10, 5)
params_to_prune = (model.weight,)
pruning_method = prune.L1Unstructured
amount = 0.3

# Task 3: Call the API
prune.random_unstructured(params_to_prune, pruning_method=pruning_method, amount=amount)