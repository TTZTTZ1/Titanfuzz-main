import torch

# Prepare valid input data
p = 0.7  # Scalar value within the range [0, 1]

# Call the API
result = torch.tensor([0.5, 0.8, 0.3]).bernoulli_(p)