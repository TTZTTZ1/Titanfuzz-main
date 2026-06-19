import torch
probs = torch.tensor(0.7)
logits = None
dist = torch.distributions.geometric.Geometric(probs=probs, logits=logits, validate_args=False)