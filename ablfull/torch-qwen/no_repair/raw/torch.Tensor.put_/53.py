import torch

# Prepare input data
index = torch.tensor([0, 2])
source = torch.tensor([4, 6])

# Call the API
result = torch.zeros(5).put_(index, source)
print(result)