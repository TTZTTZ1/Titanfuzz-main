import torch

# Prepare valid input data
p = torch.tensor([0.5])

# Call the API
result = torch.tensor([0.0]).bernoulli_(p)

print(result)