import torch
from torch.nn.utils.prune import random_unstructured

# Task 2: Generate input data
module = torch.nn.Linear(in_features=10, out_features=5)
params_to_prune = (module, 'weight')

# Task 3: Call the API
random_unstructured(params_to_prune, name='weight', amount=0.2)