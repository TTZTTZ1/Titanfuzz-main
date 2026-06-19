import torch
probs = torch.tensor(0.5)
dist = torch.distributions.geometric.Geometric(probs)