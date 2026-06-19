import torch
probs = torch.tensor(0.5)
geometric_distribution = torch.distributions.geometric.Geometric(probs=probs)