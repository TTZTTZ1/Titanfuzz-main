import torch

# Task 2: Generate input data
total_count = torch.tensor(5.0)
probs = torch.tensor(0.3)

# Task 3: Call the API
nb_dist = torch.distributions.negative_binomial.NegativeBinomial(total_count, probs=probs)