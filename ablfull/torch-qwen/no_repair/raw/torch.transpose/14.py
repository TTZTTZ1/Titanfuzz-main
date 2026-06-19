import torch

# Generate input data
x = torch.randn(2, 3)

# Call the API
result = torch.transpose(x, 0, 1)