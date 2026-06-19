import torch
from torch.nn.utils import prune

# Generate input data
module = torch.nn.Linear(10, 5)
params_to_prune = (module, 'weight')

# Call the API
prune.random_unstructured(*params_to_prune, amount=0.1)