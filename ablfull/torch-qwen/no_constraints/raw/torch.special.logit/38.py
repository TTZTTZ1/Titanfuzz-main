import torch

# Prepare valid input data
x = torch.tensor([0.1, 0.4, 0.6, 0.9])

# Call the API
result = torch.special.logit(x)

print(result)