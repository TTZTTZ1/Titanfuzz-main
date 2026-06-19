import torch

# Task 2: Generate input data
model = torch.nn.Linear(10, 5)
params_to_prune = (model, 'weight')

# Task 3: Call the API
torch.nn.utils.prune.random_unstructured(*params_to_prune, amount=0.2)