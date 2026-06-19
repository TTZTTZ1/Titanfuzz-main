import torch

# Prepare input data
model = torch.nn.Linear(10, 5)
name = 'weight'
amount = 0.5

# Call the target API
torch.nn.utils.prune.random_unstructured(model, name, amount)