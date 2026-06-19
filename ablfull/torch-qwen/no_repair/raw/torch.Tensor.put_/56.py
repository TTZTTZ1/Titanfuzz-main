import torch

# Generate valid input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([99, 88, 77])

# Call the API
result = torch.tensor([1, 2, 3]).put_(index, source)
print(result)