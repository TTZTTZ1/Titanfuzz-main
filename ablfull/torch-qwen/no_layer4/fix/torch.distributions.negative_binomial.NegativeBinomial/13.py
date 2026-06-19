import torch
total_count = torch.tensor(5.0)
probs = torch.tensor(0.6)
logits = None
validate_args = False
nb_dist = torch.distributions.negative_binomial.NegativeBinomial(total_count=total_count, probs=probs, logits=logits, validate_args=validate_args)