import torch
from torch.nn.utils import prune

# Step 1: Import PyTorch (already done implicitly by the task description)

# Step 2: Generate input data
module = torch.nn.Linear(in_features=10, out_features=5)
name = 'weight'
amount = 0.2  # Example float within the specified range [0.0, 1.0]

# Step 3: Call the API
pruned_module = prune.random_unstructured(module, name=name, amount=amount)