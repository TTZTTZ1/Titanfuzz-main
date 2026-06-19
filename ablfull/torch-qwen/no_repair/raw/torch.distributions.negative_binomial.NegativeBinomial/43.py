import torch

# Generate input data
total_count = torch.tensor(5.0)
probs = torch.tensor(0.6)
logits = None
validate_args = False

# Call the API
distribution = torch.distributions.negative_binomial.NegativeBinomial(total_count=total_count, probs=probs, validate_args=validate_args)