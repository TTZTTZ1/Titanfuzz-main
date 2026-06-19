import torch
from torch.nn.utils.prune import random_unstructured

# Step 2: Generate input data
module = torch.nn.Linear(5, 2)
name = 'weight'
amount = 0.5

# Step 3: Call the API
random_unstructured(module, name, amount=amount)