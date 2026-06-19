import torch

probs = torch.tensor(0.5)
geometric_dist = torch.distributions.geometric.Geometric(probs=probs)