import torch

# Generate valid input data
total_count = 10
probs = torch.tensor(0.5)
validate_args = True

# Call the API
distribution = torch.distributions.negative_binomial.NegativeBinomial(total_count, probs=probs, validate_args=validate_args)