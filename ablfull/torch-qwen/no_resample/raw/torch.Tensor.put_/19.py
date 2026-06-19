import torch

# Prepare valid input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([9, 8, 7])

# Call the API
result = torch.zeros(5)
result.put_(index, source)

print(result)