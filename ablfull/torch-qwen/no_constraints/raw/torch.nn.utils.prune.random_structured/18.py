import torch
from torch.nn.utils import prune

# Task 2: Generate input data
model = torch.nn.Linear(10, 5)
params_to_prune = (
    (model, 'weight'),
)
amount = {param: 0.3 for param in params_to_prune}

# Task 3: Call the API
prune.random_structured(*params_to_prune, amount=amount)