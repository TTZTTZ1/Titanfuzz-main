import torch

# Prepare valid input data
a = torch.tensor([1, 2, 3], dtype=torch.int)
b = torch.tensor([4, 5, 6], dtype=torch.int)

# Call the API
result = torch.add(a, b)