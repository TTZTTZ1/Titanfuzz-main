import torch

# Generate valid input data
probs = torch.tensor(0.5)

# Call the API
distribution = torch.distributions.geometric.Geometric(probs=probs)