import torch

# Prepare input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([7, 8, 9])

# Call the API
result = torch.zeros(5)
result.put_(index, source)

print(result)