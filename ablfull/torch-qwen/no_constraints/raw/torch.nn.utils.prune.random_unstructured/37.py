import torch
from torch.nn.utils.prune import random_unstructured

# Task 2: Generate input data
module = torch.nn.Linear(10, 5)
parameters_to_prune = ('weight',)
pruning_amount = 0.2

# Task 3: Call the API
random_unstructured(module, name=parameters_to_prune[0], amount=pruning_amount)