import torch

# Prepare input data
index = torch.tensor([0, 1, 2], dtype=torch.int)
source = torch.tensor([9, 8, 7], dtype=torch.float)

# Call the API
result = torch.zeros(3, dtype=torch.float)
result.put_(index, source)
print(result)