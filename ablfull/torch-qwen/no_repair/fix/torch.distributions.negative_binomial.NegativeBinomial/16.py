
import torch
total_count = torch.tensor(5)
probs = torch.tensor(0.7)
dist = torch.distributions.negative_binomial.NegativeBinomial(total_count=total_count, probs=probs)
