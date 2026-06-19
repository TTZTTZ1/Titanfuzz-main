import torch
from torch.nn.utils import prune

# Step 2: Generate input data
module = torch.nn.Linear(5, 3)
name = 'weight'
amount = 0.5
dim = 0

# Step 3: Call the API
prune.random_structured(module, name, amount, dim)