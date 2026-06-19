import torch

probs = 0.75
validate_args = False

geometric_dist = torch.distributions.geometric.Geometric(probs=probs, validate_args=validate_args)