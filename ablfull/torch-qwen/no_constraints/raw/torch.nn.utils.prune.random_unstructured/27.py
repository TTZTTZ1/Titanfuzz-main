import torch
from torch.nn.utils import prune

# Task 2: Generate input data
model = torch.nn.Linear(10, 5)
parameters_to_prune = (model.weight,)
pruning_method = prune.L1Unstructured(pruning_amount=0.2)

# Task 3: Call the API
prune.random_unstructured(parameters_to_prune, pruning_method)