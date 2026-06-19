import torch

# Prepare input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([9, 8, 7])

# Call the API
result = torch.empty(3)
result.put_(index, source)

print(result)