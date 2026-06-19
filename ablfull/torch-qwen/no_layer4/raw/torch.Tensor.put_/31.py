import torch

# Generate input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([10, 20, 30])

# Call the API
result = torch.tensor([0, 0, 0]).put_(index, source)
print(result)