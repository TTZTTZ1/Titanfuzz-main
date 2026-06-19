import torch

# Generate input data
probs = torch.tensor(0.5)

# Call the API
torch.distributions.geometric.Geometric(probs=probs)