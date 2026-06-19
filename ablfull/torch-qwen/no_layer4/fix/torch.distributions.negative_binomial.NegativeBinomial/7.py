import torch
total_count = torch.tensor(5.0)
probs = torch.tensor(0.7)
validate_args = False
distribution = torch.distributions.negative_binomial.NegativeBinomial(total_count=total_count, probs=probs, validate_args=validate_args)