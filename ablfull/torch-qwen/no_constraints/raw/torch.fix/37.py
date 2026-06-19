import torch

# Prepare valid input data
x = torch.tensor([-0.5, 0.0, 0.5, 1.5])

# Call the API
result = torch.fix(x)

print(result)