
import torch
probs = torch.tensor(0.7)
logits = None
validate_args = True
geometric_distribution = torch.distributions.geometric.Geometric(probs=probs, logits=logits, validate_args=validate_args)
