import torch

# Generate input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([7, 8, 9])

# Call the API
result = torch.Tensor([5, 6, 7]).put_(index, source)

print(result)