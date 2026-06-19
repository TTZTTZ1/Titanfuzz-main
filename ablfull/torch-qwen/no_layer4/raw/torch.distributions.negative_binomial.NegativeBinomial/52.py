import torch

# Generate input data
total_count = torch.tensor(5)
probs = torch.tensor(0.7)
validate_args = True

# Call the API
nb_dist = torch.distributions.negative_binomial.NegativeBinomial(total_count, probs=probs, validate_args=validate_args)