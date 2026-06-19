import torch

# Prepare input data
total_count = torch.tensor(5.0)
probs = torch.tensor(0.3)

# Call the API
distribution = torch.distributions.negative_binomial.NegativeBinomial(total_count, probs=probs)