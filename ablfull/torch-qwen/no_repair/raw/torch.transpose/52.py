import torch

# Generate input data
a = torch.randn(2, 3)

# Call the API
result = torch.transpose(a, 0, 1)