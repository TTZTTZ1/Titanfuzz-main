import torch

# Generate input data
p = 0.7  # Scalar float within the range [0, 1]

# Call the API
result = torch.tensor([0, 1]).bernoulli_(p)

print(result)