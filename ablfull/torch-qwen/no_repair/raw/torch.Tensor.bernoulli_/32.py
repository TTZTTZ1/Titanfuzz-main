import torch

# Prepare valid input data
p = 0.7  # Scalar value within [0, 1]

# Call the API
result = torch.tensor([1.0, 0.0]).bernoulli_(p)

print(result)