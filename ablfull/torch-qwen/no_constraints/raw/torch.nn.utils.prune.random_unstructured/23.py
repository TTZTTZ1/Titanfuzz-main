import torch
from torch.nn.utils import prune

# Task 2: Generate input data
model = torch.nn.Linear(5, 3)
pruning_mask = prune.random_unstructured(model.weight, name="weight", amount=0.2)

# Task 3: Call the API
pruned_model = prune.remove(pruning_mask, name="weight")