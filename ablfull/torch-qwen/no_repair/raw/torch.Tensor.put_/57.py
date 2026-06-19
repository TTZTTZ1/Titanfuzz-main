import torch

# Prepare input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([99, 88, 77])

# Call the API
result = torch.zeros(3).put_(index, source)
print(result)