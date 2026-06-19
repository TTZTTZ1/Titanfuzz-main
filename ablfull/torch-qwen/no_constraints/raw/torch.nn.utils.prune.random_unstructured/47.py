import torch

# Task 2: Generate input data
model = torch.nn.Linear(10, 5)
params_to_prune = (
    (model, 'weight'),
)

# Task 3: Call the API
pruned_model = torch.nn.utils.prune.random_unstructured(model, name='weight', amount=0.2)