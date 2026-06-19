import torch
probs = torch.tensor(0.5)
logits = None
dist = torch.distributions.geometric.Geometric(probs=probs, logits=logits)