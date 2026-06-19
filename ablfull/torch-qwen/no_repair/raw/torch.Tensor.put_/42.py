import torch

# Prepare valid input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([10, 20, 30])

# Call the API
result = torch.zeros(3)
result.put_(index, source)

print(result)