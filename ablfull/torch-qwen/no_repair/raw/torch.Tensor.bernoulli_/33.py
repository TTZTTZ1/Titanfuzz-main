import torch

# Prepare valid input data
p = torch.tensor(0.7)

# Call the API
result = torch.rand_like(p)
result.bernoulli_(p)