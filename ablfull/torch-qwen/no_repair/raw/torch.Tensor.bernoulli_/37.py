import torch

# Prepare valid input data
p = torch.tensor(0.7)  # Scalar float within the range [0, 1]

# Call the API
result = torch.empty((3, 3)).bernoulli_(p)