
import torch
probs = 0.5
validate_args = False
dist = torch.distributions.Geometric(probs=probs, validate_args=validate_args)
