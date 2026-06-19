import torch

# Prepare input data
index = torch.tensor([0, 1, 2], dtype=torch.int)
source = torch.tensor([3, 4, 5], dtype=torch.float)
accumulate = False

# Call the API
result = torch.zeros(3).put_(index, source, accumulate=accumulate)
print(result)