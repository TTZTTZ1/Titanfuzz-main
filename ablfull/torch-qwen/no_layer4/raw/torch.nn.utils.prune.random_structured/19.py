import torch
import torch.nn as nn

# Step 2: Generate input data
module = nn.Linear(10, 5)
name = 'weight'
amount = 0.5
dim = 0

# Step 3: Call the API
pruned_module = torch.nn.utils.prune.random_structured(module, name, amount, dim)