import torch
probs = torch.tensor(0.5)
distribution = torch.distributions.geometric.Geometric(probs)