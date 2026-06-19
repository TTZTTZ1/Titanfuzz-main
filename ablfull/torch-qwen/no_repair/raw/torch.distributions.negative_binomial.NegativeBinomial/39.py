import torch

# Prepare valid input data
total_count = torch.tensor(5)
probs = torch.tensor(0.6)

# Call the API
negative_binomial_dist = torch.distributions.negative_binomial.NegativeBinomial(total_count=total_count, probs=probs)