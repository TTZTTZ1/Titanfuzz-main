import torch

# Prepare valid input data
p = 0.7  # Scalar value within [0, 1]
generator = None  # Default value

# Call the API
result = torch.tensor([0.5, 0.8]).bernoulli_(p, generator=generator)
print(result)