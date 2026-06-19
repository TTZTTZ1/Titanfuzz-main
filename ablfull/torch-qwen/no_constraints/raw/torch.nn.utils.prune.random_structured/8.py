import torch
from torch.nn.utils import prune

# Prepare valid input data
model = torch.nn.Linear(5, 3)
params_to_prune = (
    (model, 'weight'),
)
amount = {name: 0.3 for name, _ in params_to_prune}

# Call the API
prune.random_structured(*params_to_prune, amount=amount)