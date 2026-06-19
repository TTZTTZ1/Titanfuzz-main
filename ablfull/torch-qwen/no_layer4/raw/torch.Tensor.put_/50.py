import torch

# Generate valid input data
index = torch.tensor([0, 2])
source = torch.tensor([7, 9])

# Call the API
result = torch.zeros(5).put_(index, source)