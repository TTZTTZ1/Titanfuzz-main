import torch

# Generate input data
p = 0.7

# Call the API
result = torch.tensor([0.5, 0.8]).bernoulli_(p)