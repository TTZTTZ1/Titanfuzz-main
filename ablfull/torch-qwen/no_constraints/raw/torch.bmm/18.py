import torch

# Generate input data
a = torch.randn(10, 3, 5)
b = torch.randn(10, 5, 4)

# Call the API
result = torch.bmm(a, b)