import torch

probs = torch.tensor(0.5)
validate_args = False

distribution = torch.distributions.geometric.Geometric(probs=probs, validate_args=validate_args)