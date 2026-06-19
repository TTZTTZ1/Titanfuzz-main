import torch

# Generate input data
p = torch.tensor(0.7)

# Call the API
result = p.bernoulli_()