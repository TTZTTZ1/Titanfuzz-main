import torch
total_count = torch.tensor(5)
probs = torch.tensor(0.6)
nb_dist = torch.distributions.negative_binomial.NegativeBinomial(total_count=total_count, probs=probs)