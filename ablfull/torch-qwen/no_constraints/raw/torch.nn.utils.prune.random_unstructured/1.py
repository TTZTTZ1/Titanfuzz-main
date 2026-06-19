import torch
from torch.nn.utils import prune

# Step 2: Generate input data
model = torch.nn.Linear(10, 5)
params_to_prune = (
    (model, 'weight'),
)

# Step 3: Call the API
prune.random_unstructured(params_to_prune, name='weight', amount=0.2)