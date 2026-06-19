import torch

# Prepare valid input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([42, 99, 65])

# Call the API
result = torch.empty(3)
result.put_(index, source)

print(result)