import torch

# Generate valid input data
index = torch.tensor([0, 2])
source = torch.tensor([4, 5])

# Call the API
result = torch.tensor([1, 2, 3]).put_(index, source)
print(result)