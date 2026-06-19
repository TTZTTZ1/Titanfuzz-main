import torch

# Task 2: Generate input data
probs = torch.tensor(0.5)
validate_args = False

# Task 3: Call the API
dist = torch.distributions.geometric.Geometric(probs=probs, validate_args=validate_args)