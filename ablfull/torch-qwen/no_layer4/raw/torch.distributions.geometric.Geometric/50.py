import torch

probs = torch.tensor(0.5)
validate_args = False

geometric_dist = torch.distributions.geometric.Geometric(probs=probs, validate_args=validate_args)