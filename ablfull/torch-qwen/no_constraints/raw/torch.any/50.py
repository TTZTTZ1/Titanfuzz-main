import torch

# Prepare valid input data
x = torch.tensor([False, False, True])

# Call the API
result = torch.any(x)

print(result)