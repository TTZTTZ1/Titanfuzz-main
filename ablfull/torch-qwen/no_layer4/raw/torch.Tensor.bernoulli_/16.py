import torch

# Prepare valid input data
p = 0.75  # Scalar value within the range [0, 1]

# Call the API
result = torch.tensor([0.1, 0.4, 0.8]).bernoulli_(p)
print(result)