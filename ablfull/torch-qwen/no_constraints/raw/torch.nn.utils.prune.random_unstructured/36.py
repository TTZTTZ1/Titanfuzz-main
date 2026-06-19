import torch
from torch.nn.utils import prune

# Prepare valid input data
model = torch.nn.Linear(10, 5)
params_to_prune = (model.weight,)
amount = 0.3

# Call the API
prune.random_unstructured(params_to_prune, name="weight", amount=amount)