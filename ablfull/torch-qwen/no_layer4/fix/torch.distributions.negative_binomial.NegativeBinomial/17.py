import torch
total_count = 10
probs = torch.tensor(0.5)
validate_args = True
distribution = torch.distributions.negative_binomial.NegativeBinomial(total_count, probs=probs, validate_args=validate_args)