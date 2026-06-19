import torch

# Prepare input data
p = 0.7  # Scalar value within the range [0, 1]

# Call the API
result = torch.tensor([0.0, 1.0]).bernoulli_(p)
print(result)