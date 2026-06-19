import torch

# Generate input data
a = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float)
other = torch.tensor([1.0, 2.5, 3.0], dtype=torch.float)

# Call the API
result = a.ne(other)