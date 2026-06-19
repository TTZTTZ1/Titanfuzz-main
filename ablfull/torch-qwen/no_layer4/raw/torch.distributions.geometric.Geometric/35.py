import torch

# Generate valid input data
probs = torch.tensor(0.5)
validate_args = False

# Call the API
distribution = torch.distributions.geometric.Geometric(probs=probs, validate_args=validate_args)