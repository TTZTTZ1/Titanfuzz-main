import torch

# Prepare valid input data
total_count = torch.tensor(5.0)
probs = torch.tensor(0.7)
validate_args = False

# Call the API
distribution = torch.distributions.negative_binomial.NegativeBinomial(total_count=total_count, probs=probs, validate_args=validate_args)