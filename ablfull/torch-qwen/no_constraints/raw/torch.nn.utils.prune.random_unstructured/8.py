import torch
from torch.nn.utils import prune

# Task 2: Generate input data
module = torch.nn.Linear(10, 5)
params_to_prune = (module, 'weight')

# Task 3: Call the API
prune.random_unstructured(*params_to_prune, amount=0.2)