import torch

# Prepare valid input data
probs = torch.tensor(0.7)
validate_args = False

# Call the API
dist = torch.distributions.geometric.Geometric(probs=probs, validate_args=validate_args)