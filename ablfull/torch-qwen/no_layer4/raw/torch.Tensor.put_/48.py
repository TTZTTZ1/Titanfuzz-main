import torch

# Generate input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([3, 4, 5])

# Call the API
result = index.put_(source)