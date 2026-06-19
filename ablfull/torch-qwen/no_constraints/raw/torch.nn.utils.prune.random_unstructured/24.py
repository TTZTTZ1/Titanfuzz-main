import torch

# Task 2: Generate input data
module = torch.nn.Linear(10, 5)
params_to_prune = (module.weight,)
amount = 0.2

# Task 3: Call the API
torch.nn.utils.prune.random_unstructured(module, name="weight", amount=amount)