import torch
total_count = torch.tensor(5.0)
probs = torch.tensor(0.7)
dist = torch.distributions.negative_binomial.NegativeBinomial(total_count, probs=probs)