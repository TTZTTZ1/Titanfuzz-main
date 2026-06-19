import torch
import torch.nn as nn

# Task 2: Generate input data
model = nn.Linear(10, 5)
params_to_prune = (model.weight,)
amount = {model.weight: 0.2}

# Task 3: Call the API
torch.nn.utils.prune.random_structured(params_to_prune, name='weight', amount=amount)