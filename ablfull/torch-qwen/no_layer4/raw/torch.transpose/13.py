import torch

# Generate input data
x = torch.randn(4, 5)

# Call the API
result = torch.transpose(x, 0, 1)