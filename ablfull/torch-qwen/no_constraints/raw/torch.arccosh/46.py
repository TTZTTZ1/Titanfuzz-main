import torch

# Generate valid input data satisfying the constraint x >= 1
x = torch.tensor(2.0)

# Call the API torch.arccosh exactly once
result = torch.arccosh(x)