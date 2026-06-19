import torch

# Generate valid input data
probs = torch.tensor(0.5)

# Call the API
geometric_dist = torch.distributions.geometric.Geometric(probs=probs)