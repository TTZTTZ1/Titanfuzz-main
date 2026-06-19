import torch

# Prepare valid input data
probs = torch.tensor(0.5)

# Call the API
dist = torch.distributions.geometric.Geometric(probs)