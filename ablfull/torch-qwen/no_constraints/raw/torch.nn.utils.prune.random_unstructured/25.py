import torch
from torch.nn.utils import prune

# Prepare valid input data
model = torch.nn.Linear(10, 5)
params_to_prune = (model.weight,)
pruning_method = prune.RandomUnstructured

# Call the API
pruned_model = prune.random_unstructured(model, name="weight", amount=0.2)