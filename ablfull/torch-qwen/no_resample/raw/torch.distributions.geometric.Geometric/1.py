import torch

# Prepare valid input data
probs = torch.tensor(0.5)
validate_args = True

# Call the API
geometric_dist = torch.distributions.geometric.Geometric(probs=probs, validate_args=validate_args)