import torch
import torch.nn as nn

# Step 1: Import PyTorch

# Step 2: Generate input data
module = nn.Linear(10, 5)
name = 'weight'
amount = 0.5

# Step 3: Call the API
pruned_module = torch.nn.utils.prune.random_unstructured(module, name, amount)