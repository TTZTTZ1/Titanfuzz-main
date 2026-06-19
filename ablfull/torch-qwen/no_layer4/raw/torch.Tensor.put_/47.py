import torch

# Prepare input data
index = torch.tensor([0, 2, 4], dtype=torch.int)
source = torch.tensor([10, 20, 30], dtype=torch.float)

# Call the API
result = torch.zeros(5, dtype=torch.float)
result.put_(index, source)