import torch
from torch.nn.utils import prune

# Step 2: Generate input data
module = torch.nn.Linear(5, 3)
params_to_prune = (module, 'weight')

# Step 3: Call the API
prune.random_unstructured(params_to_prune, name='weight', amount=0.5)