import torch
import torch.nn as nn

# Task 2: Generate input data
module = nn.Linear(in_features=10, out_features=5)
params_to_prune = ((module, 'weight'),)

# Task 3: Call the API
pruned_module = torch.nn.utils.prune.random_unstructured(module, name='weight', amount=0.2)