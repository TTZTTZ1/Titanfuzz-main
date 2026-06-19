import torch
import torch.nn as nn

# Step 2: Generate input data
module = nn.Linear(5, 3)
parameters_to_prune = (module, 'weight')

# Step 3: Call the API
pruned_module = torch.nn.utils.prune.random_unstructured(*parameters_to_prune, amount=0.2)