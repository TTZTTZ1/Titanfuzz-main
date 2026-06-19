import torch

# Prepare input data
a = torch.randn(5, 10)
b = torch.randn(5, 10)

# Call the API
result = torch.bmm(a, b)