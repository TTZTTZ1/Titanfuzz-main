import torch
from torch.nn.utils import prune

# Prepare input data
module = torch.nn.Linear(10, 5)
params_to_prune = (module, 'weight')
amount = 0.3

# Call the API
prune.random_unstructured(params_to_prune, name='weight', amount=amount)