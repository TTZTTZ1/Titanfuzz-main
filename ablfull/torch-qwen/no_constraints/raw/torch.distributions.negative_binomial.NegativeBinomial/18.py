import torch

# Task 2: Generate input data
total_count = torch.tensor(5.0)
probs = torch.tensor(0.6)

# Task 3: Call the API
dist = torch.distributions.negative_binomial.NegativeBinomial(total_count, probs=probs)