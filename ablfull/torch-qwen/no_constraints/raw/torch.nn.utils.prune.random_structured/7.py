import torch
from torch.nn.utils import prune

# Task 2: Generate input data
model = torch.nn.Linear(10, 5)
params_to_prune = (model.weight,)
amount = {model.weight: 0.2}

# Task 3: Call the API
prune.random_structured(*params_to_prune, amount=amount)