import torch
from torch.nn.utils import prune

# Step 2: Generate input data
model = torch.nn.Linear(10, 5)
name = 'weight'
amount = 0.5

# Step 3: Call the API
prune.random_unstructured(model, name, amount)