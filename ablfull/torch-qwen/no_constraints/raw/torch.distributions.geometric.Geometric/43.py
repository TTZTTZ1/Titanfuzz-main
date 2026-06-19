import torch

# Prepare valid input data
probs = torch.tensor(0.5)

# Call the target API
dist = torch.distributions.geometric.Geometric(probs=probs)