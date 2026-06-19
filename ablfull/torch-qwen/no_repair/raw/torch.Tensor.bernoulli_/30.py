import torch

# Prepare valid input data
p = 0.7

# Call the API
result = torch.tensor([0.1, 0.9]).bernoulli_(p)
print(result)