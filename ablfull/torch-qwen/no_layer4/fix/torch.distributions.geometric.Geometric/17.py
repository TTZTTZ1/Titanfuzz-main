import torch
probs = torch.tensor(0.7)
validate_args = False
result = torch.distributions.geometric.Geometric(probs=probs, validate_args=validate_args)