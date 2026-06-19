import torch

# Prepare input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([4, 5, 6])

# Call the API
result = torch.tensor([7, 8, 9]).put_(index, source)
print(result)