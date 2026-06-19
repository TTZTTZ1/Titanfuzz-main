import torch

# Prepare valid input data
p = 0.7  # Scalar value within [0, 1]

# Call the API
result = torch.tensor([0.1, 0.4, 0.6]).bernoulli_(p)
print(result)