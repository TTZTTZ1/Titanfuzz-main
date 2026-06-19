import torch

# Prepare valid input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([4, 5, 6])

# Call the API
result = torch.zeros(3)
result.put_(index, source)

print(result)