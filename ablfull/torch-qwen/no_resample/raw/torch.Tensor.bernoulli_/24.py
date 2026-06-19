import torch

# Prepare valid input data
p = 0.7

# Call the API
result = torch.tensor([0.3, 0.8]).bernoulli_(p)
print(result)