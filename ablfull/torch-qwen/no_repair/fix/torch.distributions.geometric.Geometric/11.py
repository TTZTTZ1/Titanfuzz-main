
import torch
probs = torch.tensor(0.5)
logits = None
validate_args = False
result = torch.distributions.geometric.Geometric(probs=probs, logits=logits, validate_args=validate_args)
