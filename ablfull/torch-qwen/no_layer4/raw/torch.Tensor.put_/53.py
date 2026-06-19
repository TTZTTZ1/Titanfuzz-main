import torch

# Generate input data
index = torch.tensor([0, 1])
source = torch.tensor([42, 99])

# Call the API
result = torch.zeros(3)
result.put_(index, source)

print(result)