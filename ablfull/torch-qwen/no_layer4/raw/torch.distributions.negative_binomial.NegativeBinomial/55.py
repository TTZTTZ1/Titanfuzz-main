import torch

# Prepare valid input data
total_count = torch.tensor(5, dtype=torch.float)
probs = torch.tensor(0.7, dtype=torch.float)

# Call the API
dist = torch.distributions.negative_binomial.NegativeBinomial(total_count=total_count, probs=probs)