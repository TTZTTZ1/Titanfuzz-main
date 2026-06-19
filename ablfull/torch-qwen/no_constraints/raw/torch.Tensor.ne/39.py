import torch

# Generate input data
x = torch.tensor([1, 2, 3])
y = torch.tensor([1, 0, 3])

# Call the API
result = x.ne(y)